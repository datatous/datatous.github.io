# -*- coding: utf-8 -*-
"""datatous — 관리자 인라인 편집용 로컬 저장 서버.

브라우저(admin.js)에서 보낸 "바뀌기 전 텍스트 → 바뀐 텍스트" 쌍을 받아
원본 소스 파일에서 그 문자열만 정확히(유일하게 일치할 때만) 교체한다.
HTML→Markdown 변환을 하지 않으므로 커스텀 컴포넌트/Liquid 태그가 안전하다.

핵심 안전장치
- 원본 문자열이 파일에 정확히 1번 등장할 때만 교체. 0번(못 찾음)/2번 이상(모호)이면 건너뛰고 사유를 리포트.
- repo 밖 경로(../ 등)·허용 외 확장자는 거부.
- 저장 후에도 git 커밋은 사람이 직접(리뷰 후). 이 서버는 working tree만 건드린다.

이 서버는 Jekyll 없이도 테스트할 수 있도록 "미리보기"도 내장한다:
- 정적 파일(assets 등)을 그대로 서빙
- 라이트 Liquid 셰임 + 마크다운 렌더로 홈/페이지/게시글을 대충 렌더 (편집 테스트용)

실행:
    python tools/admin_edit_server.py            # 기본 포트 4001
    python tools/admin_edit_server.py --port 4005

브라우저에서 http://localhost:4001 접속 → 미리보기 목록 → Ctrl+Shift+E 로 편집 모드.
(실제 발행은 평소처럼 git push → GitHub Pages 렌더)
"""
import argparse
import html as _html
import json
import mimetypes
import re
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

try:
    import markdown as _md
except Exception:
    _md = None

# Windows PowerShell(cp949) 콘솔에서도 한글 로그가 깨지지 않도록
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

# repo 루트 = 이 스크립트(tools/…)의 부모의 부모
REPO_ROOT = Path(__file__).resolve().parent.parent
ALLOWED_SUFFIXES = {".md", ".markdown", ".html", ".htm", ".yml", ".yaml"}

# admin.js 의 normText 와 동일한 정규화(연속 공백 → 한 칸, 앞뒤 trim, NBSP 처리)
_WS = re.compile(r"\s+")


def norm(s: str) -> str:
    return _WS.sub(" ", s.replace(" ", " ")).strip()


def resolve_src(src: str) -> Path:
    """repo 내부의 안전한 경로로만 해석. 아니면 ValueError."""
    src = (src or "").lstrip("/").replace("\\", "/")
    if not src:
        raise ValueError("빈 경로")
    full = (REPO_ROOT / src).resolve()
    if REPO_ROOT not in full.parents and full != REPO_ROOT:
        raise ValueError("repo 밖 경로 거부")
    if full.suffix.lower() not in ALLOWED_SUFFIXES:
        raise ValueError("허용되지 않는 파일 형식: " + full.suffix)
    if not full.is_file():
        raise ValueError("파일이 없음: " + src)
    return full


def find_and_replace(text: str, original: str, updated: str):
    """original 을 유일하게 찾아 교체한 새 텍스트를 반환. (new_text, message) or (None, 사유)."""
    # 1) 원문 그대로
    for needle in _candidates(original):
        n = text.count(needle)
        if n == 1:
            return text.replace(needle, _sub_repl(needle, original, updated), 1), None
        if n > 1:
            return None, f'원본이 파일에 {n}번 등장(모호) — 수동 수정 필요: "{_clip(original)}"'
    return None, f'원본 텍스트를 파일에서 못 찾음(인라인 서식/줄바꿈일 수 있음): "{_clip(original)}"'


def _candidates(original: str):
    """원본 텍스트를 파일에서 찾기 위한 후보 문자열들(정규화 편차 흡수)."""
    seen = []
    for c in (original, original.strip()):
        if c and c not in seen:
            seen.append(c)
    return seen


def _sub_repl(needle: str, original: str, updated: str) -> str:
    """needle 이 original 을 감싼 형태(앞뒤 공백 차이)일 때 공백은 보존."""
    lead = needle[: len(needle) - len(needle.lstrip())]
    trail = needle[len(needle.rstrip()):]
    return lead + updated.strip() + trail


def _clip(s: str, n: int = 42) -> str:
    s = s.replace("\n", " ")
    return s if len(s) <= n else s[:n] + "…"


# ==========================================================================
#  미리보기 렌더 (Jekyll 없이 테스트용) — 대충 렌더이며 발행물과 다를 수 있음
# ==========================================================================
_FM = re.compile(r"^---\s*\n.*?\n---\s*\n?", re.DOTALL)
_LIQ_URL = re.compile(r"\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*(?:relative_url|absolute_url)\s*\}\}")
_LIQ_BLOCK = re.compile(r"\{%-?\s*(for|if|unless)\b.*?%\}.*?\{%-?\s*end\1\s*-?%\}", re.DOTALL)
_LIQ_TAG = re.compile(r"\{%-?.*?-?%\}", re.DOTALL)
_LIQ_OUT = re.compile(r"\{\{.*?\}\}", re.DOTALL)


def strip_front_matter(text):
    m = _FM.match(text)
    fm = {}
    if m:
        raw = m.group(0)
        body = text[m.end():]
        for line in raw.splitlines():
            mm = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip().strip("\"'")
        return fm, body
    return fm, text


def liquid_shim(text):
    text = _LIQ_URL.sub(r"\1", text)
    text = _LIQ_BLOCK.sub("", text)
    text = _LIQ_TAG.sub("", text)
    text = _LIQ_OUT.sub("", text)
    return text


PAGE_TMPL = """<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>preview — {title}</title>
<meta name="gh-source" content="{src}">
<link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/admin.css">
<script src="/assets/js/admin.js" defer></script>
<style>
 body{{font-family:'Pretendard',sans-serif;color:#1f2937;line-height:1.7;
   max-width:820px;margin:0 auto;padding:60px 24px 120px;}}
 .preview-flag{{background:#fef3c7;color:#92400e;border:1px solid #fde68a;border-radius:10px;
   padding:8px 14px;font-size:.82rem;margin-bottom:24px;}}
 .page__content h1,.page__title{{font-size:1.9rem;font-weight:800;margin:.6em 0 .3em;}}
 .page__content h2{{font-size:1.4rem;font-weight:800;margin:1.2em 0 .3em;}}
 .page__content h3{{font-size:1.15rem;font-weight:700;margin:1em 0 .3em;}}
 .page__content p,.page__content li{{margin:.5em 0;}}
 .page__content img{{max-width:100%;}}
 .page__content a{{color:#2563eb;}}
 .back{{display:inline-block;margin-bottom:20px;color:#2563eb;text-decoration:none;font-weight:700;}}
</style></head><body>
<a class="back" href="/">← 미리보기 목록</a>
<div class="preview-flag">⚠️ Jekyll 없이 렌더한 <b>편집 테스트용 미리보기</b>입니다 (실제 발행물과 스타일이 다름). Ctrl+Shift+E 로 편집.</div>
{title_html}
<div class="page__content">
{body}
</div></body></html>"""


def render_preview(src, full):
    raw = full.read_text(encoding="utf-8")
    if full.suffix.lower() in (".html", ".htm"):
        # 홈 레이아웃 등 완결형 HTML — 셰임만 하고 그대로 서빙
        _, body = strip_front_matter(raw)
        return liquid_shim(body)
    # 마크다운 페이지/게시글
    fm, body = strip_front_matter(raw)
    body = liquid_shim(body)
    if _md is not None:
        body_html = _md.markdown(body, extensions=["extra", "sane_lists"])
    else:
        body_html = "<pre>" + _html.escape(body) + "</pre>"
    title = fm.get("title", full.stem)
    title_html = '<h1 class="page__title">{}</h1>'.format(_html.escape(title)) if title else ""
    return PAGE_TMPL.format(title=_html.escape(title), src=src,
                            title_html=title_html, body=body_html)


def build_index():
    def links(paths, label):
        items = []
        for p in sorted(paths):
            rel = p.relative_to(REPO_ROOT).as_posix()
            items.append('<li><a href="/preview?src={}">{}</a></li>'.format(
                urllib.parse.quote(rel), _html.escape(rel)))
        return "<h2>{}</h2><ul>{}</ul>".format(label, "".join(items)) if items else ""

    home = [REPO_ROOT / "_layouts/home_landing.html"]
    pages = list((REPO_ROOT / "_pages").glob("*.md")) if (REPO_ROOT / "_pages").is_dir() else []
    posts = list((REPO_ROOT / "_posts").glob("*.md")) if (REPO_ROOT / "_posts").is_dir() else []
    body = links(home, "메인(홈)") + links(pages, "페이지") + links(posts, "게시글")
    return ("<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'>"
            "<title>datatous 편집 미리보기</title>"
            "<style>body{font-family:sans-serif;max-width:760px;margin:40px auto;padding:0 20px;color:#1f2937}"
            "h1{font-size:1.5rem}h2{font-size:1rem;color:#2563eb;margin-top:1.6em}"
            "a{color:#2563eb;text-decoration:none}li{margin:6px 0}"
            ".hint{background:#eff6ff;border:1px solid #dbeafe;border-radius:10px;padding:12px 16px;font-size:.86rem}"
            "</style></head><body><h1>✏️ datatous 편집 미리보기</h1>"
            "<p class='hint'>페이지를 열고 <b>Ctrl+Shift+E</b> 로 편집 모드를 켜세요. 수정 → 오른쪽 아래 <b>저장</b> → 원본 파일 반영 → git 커밋.</p>"
            + body + "</body></html>")


def guess_type(path):
    t, _ = mimetypes.guess_type(str(path))
    return t or "application/octet-stream"


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        route = parsed.path

        if route == "/health":
            self._json(200, {"ok": True, "root": str(REPO_ROOT)})
            return

        if route == "/" or route == "":
            self._send_html(200, build_index())
            return

        if route == "/preview":
            q = urllib.parse.parse_qs(parsed.query)
            src = (q.get("src") or [""])[0]
            try:
                full = resolve_src(src)
            except ValueError as e:
                self._send_html(400, "<h1>400</h1><p>" + _html.escape(str(e)) + "</p>")
                return
            try:
                self._send_html(200, render_preview(src, full))
            except Exception as e:
                self._send_html(500, "<h1>500</h1><pre>" + _html.escape(repr(e)) + "</pre>")
            return

        # 그 외 → 정적 파일 서빙 (assets 등)
        self._serve_static(urllib.parse.unquote(route))

    def _serve_static(self, route):
        rel = route.lstrip("/").replace("\\", "/")
        full = (REPO_ROOT / rel).resolve()
        if REPO_ROOT not in full.parents or not full.is_file():
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        data = full.read_bytes()
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", guess_type(full))
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_html(self, code, text):
        data = text.encode("utf-8")
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path.rstrip("/") != "/save":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            edits = payload.get("edits", [])
        except Exception as e:
            self._json(400, {"ok": False, "error": f"잘못된 요청: {e}"})
            return

        # 파일별로 묶어 순차 적용(같은 파일에 여러 수정)
        results = [None] * len(edits)
        file_cache = {}   # src -> current text
        file_dirty = {}   # src -> bool

        for i, ed in enumerate(edits):
            src = ed.get("src", "")
            original = ed.get("original", "")
            updated = ed.get("updated", "")
            if norm(original) == norm(updated):
                results[i] = {"ok": True, "message": "변경 없음"}
                continue
            try:
                full = resolve_src(src)
            except ValueError as e:
                results[i] = {"ok": False, "message": str(e)}
                continue
            key = str(full)
            if key not in file_cache:
                file_cache[key] = full.read_text(encoding="utf-8")
                file_dirty[key] = False
            new_text, msg = find_and_replace(file_cache[key], original, updated)
            if new_text is None:
                results[i] = {"ok": False, "message": msg}
            else:
                file_cache[key] = new_text
                file_dirty[key] = True
                results[i] = {"ok": True, "message": "교체됨"}

        # 실제 파일 기록 (개행 보존: newline="")
        for key, dirty in file_dirty.items():
            if dirty:
                Path(key).write_text(file_cache[key], encoding="utf-8", newline="")

        saved = sum(1 for r in results if r and r.get("ok") and r.get("message") == "교체됨")
        print(f"[save] {saved}건 저장, {len(edits) - saved}건 스킵/무변경")
        self._json(200, {"ok": True, "results": results})

    def _json(self, code, obj):
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(obj, ensure_ascii=False).encode("utf-8"))

    def log_message(self, *args):
        pass  # 기본 접근 로그 소음 억제


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=4001)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    url = f"http://localhost:{args.port}"
    print(f"datatous 편집 서버 실행 중 → {url}")
    print(f"  · 미리보기/편집:  {url}/  (열고 Ctrl+Shift+E)")
    print(f"  · repo 루트:      {REPO_ROOT}")
    if _md is None:
        print("  · (참고) python 'markdown' 미설치 → 게시글은 평문으로 보임. pip install markdown")
    print("종료: Ctrl+C")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n종료됨")


if __name__ == "__main__":
    main()
