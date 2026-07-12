/* ============================================================
   datatous — 관리자 인라인 편집 모드 (admin.js)

   무엇을 하나:
   - 로컬(localhost)에서만 활성화. 라이브 사이트(datatous.github.io)에는
     UI가 뜨지 않아 방문자에게 영향 없음.
   - Ctrl+Shift+E 또는 상단 배너로 관리자 모드 ON/OFF.
   - ON 이면 화면의 텍스트 요소를 클릭해 그 자리에서 바로 수정.
   - "저장" 누르면 로컬 헬퍼 서버(admin_edit_server.py)로 보내
     원본 .md / .html 파일에서 "바뀌기 전 문자열"만 정확히 찾아 교체한다.
     (HTML→Markdown 변환을 하지 않으므로 커스텀 컴포넌트가 깨지지 않음)

   저장이 되려면 헬퍼 서버가 떠 있어야 한다:
     python tools/admin_edit_server.py
   ============================================================ */
(function () {
  'use strict';

  // ---- 활성 조건: localhost 이거나 ?admin=1 일 때만 ------------------------
  var LOCAL = /^(localhost|127\.0\.0\.1|\[::1\]|0\.0\.0\.0)$/.test(location.hostname);
  var FORCED = /[?&]admin=1\b/.test(location.search);
  if (!LOCAL && !FORCED) return;

  var HELPER = localStorage.getItem('datatous_admin_helper') || 'http://localhost:4001';
  var STATE_KEY = 'datatous_admin_on';

  // 편집 대상 콘텐츠 컨테이너 (Minimal Mistakes 테마 페이지)
  var CONTENT_SELECTORS = [
    '.page__content', '.page__title', '.page__lead',
    '.archive__item-title', '.archive__item-excerpt'
  ];
  // 텍스트 리프 판정 시 "블록 자식"으로 취급할 태그 (이게 있으면 그 요소는 리프가 아님)
  var BLOCK = {
    DIV:1, SECTION:1, ARTICLE:1, HEADER:1, FOOTER:1, NAV:1, ASIDE:1, MAIN:1,
    UL:1, OL:1, LI:1, DL:1, DT:1, DD:1, TABLE:1, THEAD:1, TBODY:1, TFOOT:1,
    TR:1, TD:1, TH:1, FIGURE:1, FIGCAPTION:1, BLOCKQUOTE:1, HR:1, FORM:1, BR:1,
    H1:1, H2:1, H3:1, H4:1, H5:1, H6:1, P:1, PRE:1
  };
  // 아예 건드리지 않을 요소
  var SKIP = {
    SCRIPT:1, STYLE:1, PRE:1, CODE:1, TEXTAREA:1, INPUT:1, SELECT:1, OPTION:1,
    IMG:1, SVG:1, CANVAS:1, VIDEO:1, AUDIO:1, IFRAME:1, BUTTON:1, NOSCRIPT:1
  };

  var editables = [];   // 편집 대상 요소 목록
  var built = false;

  // ---- 소스 경로 결정 ------------------------------------------------------
  // 각 요소는 data-src(명시) → 가장 가까운 조상의 data-src → 페이지 meta 순으로
  // 자신이 속한 원본 파일을 안다.
  function pageSource() {
    var m = document.querySelector('meta[name="gh-source"]');
    return m && m.content ? m.content : null;
  }
  function sourceFor(el) {
    var cur = el;
    while (cur && cur.nodeType === 1) {
      if (cur.dataset && cur.dataset.src) return cur.dataset.src;
      cur = cur.parentElement;
    }
    return pageSource();
  }

  // ---- 편집 대상 수집 ------------------------------------------------------
  function normText(s) {
    return (s == null ? '' : String(s)).replace(/ /g, ' ').replace(/\s+/g, ' ').trim();
  }

  function isTextLeaf(el) {
    if (SKIP[el.tagName]) return false;
    if (el.closest && el.closest('#admin-bar, #admin-panel')) return false;
    if (!normText(el.textContent)) return false;
    // 블록 레벨 자식이 하나라도 있으면 리프가 아님 (더 안쪽 요소를 택함)
    var kids = el.children;
    for (var i = 0; i < kids.length; i++) {
      if (BLOCK[kids[i].tagName]) return false;
      if (SKIP[kids[i].tagName]) return false;
    }
    return true;
  }

  function collect() {
    var set = [];
    var seen = new Set();

    // 1) 명시적으로 표시된 요소 (홈 레이아웃 등): data-edit 속성
    document.querySelectorAll('[data-edit]').forEach(function (el) {
      if (!seen.has(el) && normText(el.textContent)) { set.push(el); seen.add(el); }
    });

    // 2) 콘텐츠 컨테이너 안의 텍스트 리프 자동 탐지
    var roots = document.querySelectorAll(CONTENT_SELECTORS.join(','));
    roots.forEach(function (root) {
      if (isTextLeaf(root)) { pushLeaf(root); return; }
      root.querySelectorAll('*').forEach(function (el) {
        if (isTextLeaf(el)) pushLeaf(el);
      });
    });

    function pushLeaf(el) {
      if (seen.has(el)) return;
      // 이미 편집 대상으로 잡힌 조상이 있으면 건너뜀 (중첩 방지)
      for (var a = el.parentElement; a; a = a.parentElement) {
        if (seen.has(a)) return;
      }
      set.push(el); seen.add(el);
    }

    return set.filter(function (el) { return sourceFor(el); });
  }

  // ---- 편집 활성/비활성 ----------------------------------------------------
  function enableEl(el) {
    el.setAttribute('data-admin-edit', '');
    el.setAttribute('contenteditable', 'true');
    el.setAttribute('spellcheck', 'false');
    if (el.dataset.orig === undefined) el.dataset.orig = normText(el.textContent);
    el.addEventListener('focus', onFocus);
    el.addEventListener('input', onInput);
    el.addEventListener('keydown', onKeydown);
    el.addEventListener('paste', onPaste);
  }
  function disableEl(el) {
    el.removeAttribute('data-admin-edit');
    el.removeAttribute('data-admin-dirty');
    el.removeAttribute('contenteditable');
    el.removeEventListener('focus', onFocus);
    el.removeEventListener('input', onInput);
    el.removeEventListener('keydown', onKeydown);
    el.removeEventListener('paste', onPaste);
  }

  function onFocus() { /* orig 은 enable 시점에 이미 고정됨 */ }
  function onInput(e) {
    var el = e.currentTarget;
    var changed = normText(el.textContent) !== el.dataset.orig;
    el.toggleAttribute('data-admin-dirty', changed);
    renderPanel();
  }
  function onKeydown(e) {
    // Enter 는 줄바꿈 대신 편집 종료 (텍스트 한 줄 편집 UX)
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); e.currentTarget.blur(); }
    if (e.key === 'Escape') {
      e.preventDefault();
      var el = e.currentTarget;
      el.textContent = el.dataset.orig;
      el.removeAttribute('data-admin-dirty');
      el.blur(); renderPanel();
    }
  }
  function onPaste(e) {
    // 서식 없는 평문만 붙여넣기
    e.preventDefault();
    var t = (e.clipboardData || window.clipboardData).getData('text/plain');
    document.execCommand('insertText', false, t.replace(/\s*\n\s*/g, ' '));
  }

  // ---- 변경분 모으기 -------------------------------------------------------
  function pendingEdits() {
    var out = [];
    editables.forEach(function (el) {
      var now = normText(el.textContent);
      if (el.dataset.orig !== undefined && now !== el.dataset.orig) {
        out.push({ el: el, src: sourceFor(el), original: el.dataset.orig, updated: now });
      }
    });
    return out;
  }

  // ---- 저장 패널 -----------------------------------------------------------
  var panel;
  function renderPanel() {
    if (!panel) return;
    var edits = pendingEdits();
    var body = panel.querySelector('.ap-body');
    var count = panel.querySelector('.ap-count');
    var saveBtn = panel.querySelector('.ap-save');
    count.textContent = edits.length;
    saveBtn.disabled = edits.length === 0;
    if (!edits.length) {
      body.innerHTML = '<div class="ap-empty">수정한 텍스트가 여기 모입니다.<br>클릭해서 고쳐보세요.</div>';
      return;
    }
    body.innerHTML = '';
    edits.forEach(function (ed) {
      var d = document.createElement('div');
      d.className = 'ap-item';
      d.innerHTML =
        '<div class="src">' + esc(ed.src) + '</div>' +
        '<div class="old">' + esc(ed.original) + '</div>' +
        '<div class="new">' + esc(ed.updated) + '</div>';
      body.appendChild(d);
    });
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function setStatus(msg, kind) {
    var s = panel.querySelector('.ap-status');
    s.textContent = msg || '';
    s.className = 'ap-status' + (kind ? ' ' + kind : '');
  }

  function save() {
    var edits = pendingEdits();
    if (!edits.length) return;
    var payload = { edits: edits.map(function (e) { return { src: e.src, original: e.original, updated: e.updated }; }) };
    var saveBtn = panel.querySelector('.ap-save');
    saveBtn.disabled = true;
    setStatus('저장 중…');
    fetch(HELPER + '/save', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(function (r) { return r.json(); })
      .then(function (res) {
        var results = res.results || [];
        var ok = 0, err = 0;
        results.forEach(function (rr, i) {
          var ed = edits[i];
          if (!ed) return;
          if (rr.ok) {
            ok++;
            ed.el.dataset.orig = ed.updated;        // 새 값을 기준선으로
            ed.el.removeAttribute('data-admin-dirty');
          } else {
            err++;
            ed.el.setAttribute('data-admin-dirty', '');
          }
        });
        renderResults(edits, results);
        if (err === 0) setStatus('✅ ' + ok + '건 저장 완료 — git으로 커밋하세요.', 'ok');
        else setStatus('일부 저장 실패: ' + ok + '건 성공 · ' + err + '건 실패 (아래 참고)', 'err');
      })
      .catch(function (e) {
        setStatus('❌ 헬퍼 서버에 연결 실패. `python tools/admin_edit_server.py` 실행 확인 (' + HELPER + ')', 'err');
        saveBtn.disabled = false;
      });
  }

  function renderResults(edits, results) {
    var body = panel.querySelector('.ap-body');
    body.innerHTML = '';
    edits.forEach(function (ed, i) {
      var rr = results[i] || { ok: false, message: '응답 없음' };
      var d = document.createElement('div');
      d.className = 'ap-item ' + (rr.ok ? 'ok' : 'err');
      d.innerHTML =
        '<div class="src">' + (rr.ok ? '✅ ' : '⚠️ ') + esc(ed.src) + '</div>' +
        '<div class="old">' + esc(ed.original) + '</div>' +
        '<div class="new">' + esc(ed.updated) + '</div>' +
        (rr.ok ? '' : '<div class="msg">' + esc(rr.message || '실패') + '</div>');
      body.appendChild(d);
    });
    panel.querySelector('.ap-count').textContent = pendingEdits().length;
  }

  // ---- UI 만들기 -----------------------------------------------------------
  function buildUI() {
    if (built) return;
    built = true;

    var bar = document.createElement('div');
    bar.id = 'admin-bar';
    bar.innerHTML =
      '<span class="ab-title">✏️ 관리자 편집 모드</span>' +
      '<span class="ab-hint">텍스트를 클릭해 수정 · Enter 확정 · Esc 취소</span>' +
      '<span class="ab-spacer"></span>' +
      '<button class="ab-off">모드 끄기 (Ctrl+Shift+E)</button>';
    document.body.appendChild(bar);
    bar.querySelector('.ab-off').addEventListener('click', function () { toggle(false); });

    panel = document.createElement('div');
    panel.id = 'admin-panel';
    panel.innerHTML =
      '<div class="ap-head"><b>변경분</b><span class="ap-count">0</span></div>' +
      '<div class="ap-body"></div>' +
      '<div class="ap-status"></div>' +
      '<div class="ap-foot">' +
      '<button class="ap-reset" title="모든 수정 되돌리기">되돌리기</button>' +
      '<button class="ap-save" disabled>저장</button>' +
      '</div>';
    document.body.appendChild(panel);
    panel.querySelector('.ap-save').addEventListener('click', save);
    panel.querySelector('.ap-reset').addEventListener('click', resetAll);
  }

  function resetAll() {
    editables.forEach(function (el) {
      if (el.dataset.orig !== undefined) el.textContent = el.dataset.orig;
      el.removeAttribute('data-admin-dirty');
    });
    setStatus('');
    renderPanel();
  }

  // ---- 모드 토글 -----------------------------------------------------------
  function toggle(on) {
    if (on === undefined) on = !document.documentElement.classList.contains('admin-on');
    if (on) {
      buildUI();
      if (!editables.length) editables = collect();
      editables.forEach(enableEl);
      document.documentElement.classList.add('admin-on');
      renderPanel();
      localStorage.setItem(STATE_KEY, '1');
      console.log('[datatous admin] 편집 대상', editables.length, '개 활성화');
    } else {
      editables.forEach(disableEl);
      document.documentElement.classList.remove('admin-on');
      localStorage.setItem(STATE_KEY, '0');
    }
  }

  // ---- 시동 ---------------------------------------------------------------
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'E' || e.key === 'e')) {
      e.preventDefault(); toggle();
    }
  });

  function boot() {
    if (localStorage.getItem(STATE_KEY) === '1' || FORCED) toggle(true);
    else console.log('[datatous admin] 대기 중 — Ctrl+Shift+E 로 편집 모드 켜기');
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
