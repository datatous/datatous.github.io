---
title: "한글(HWP) COM 문서 자동 생성의 함정과 우회"
wiki_type: concept
tags: [hwp, com-automation, windows, python, document-generation, encoding]
last_modified_at: 2026-09-07
excerpt: "Windows에서 `HWPFrame.HwpObject` COM으로 **서식이 있는 한글 문서를 자동 생성하는 것은 가능하다.** 다만 API가 성공을 반환하면서 결과물이 조용히 망가지는 구간이 셋 있다 — ① HTML 삽입 시 한글이 두부로 깨짐(인코딩) ② CP949에 없는 문자가 `?`로 사라짐 ③ **표 안 내용이 한 쪽을 넘으면 렌더에서 잘림.** "
---

<span class="wiki-type-badge">concept</span>

## Summary

Windows에서 `HWPFrame.HwpObject` COM으로 **서식이 있는 한글 문서를 자동 생성하는 것은 가능하다.** 다만 API가 성공을 반환하면서 결과물이 조용히 망가지는 구간이 셋 있다 — ① HTML 삽입 시 한글이 두부로 깨짐(인코딩) ② CP949에 없는 문자가 `?`로 사라짐 ③ **표 안 내용이 한 쪽을 넘으면 렌더에서 잘림.** 셋 다 반환값으로는 감지되지 않으므로 **매 단계 PDF로 내보내 렌더를 확인하는 것이 유일한 검증 수단**이다.

## Key Facts

- **HTML 삽입은 CP949로 해석된다.** `SetTextFile(html, "HTML", "insertfile")`은 동작하지만, HTML의 `<meta charset>`을 `utf-8`로 두면 한글이 전부 두부가 된다. **`euc-kr`로 선언하면 정상 렌더된다.** 폰트 지정으로는 해결되지 않는다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- **CP949 미지원 문자는 소실된다.** em dash `—`(U+2014)와 en dash `–`(U+2013)가 대표적이다. `—`는 `―`(U+2015)로 치환하면 통과한다. 로마 숫자·가운뎃점·곱셈기호·한글 따옴표는 CP949에 있어 안전하다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- **이 인코딩 제약은 HTML 경로에만 적용된다.** `InsertText` 액션(BSTR)으로 넣는 문자열은 유니코드가 그대로 들어간다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- 🔴 **표는 쪽을 넘기지 못한다.** 내용이 한 쪽을 넘으면 넘친 부분이 렌더되지 않는다. 문서 내부에는 텍스트가 남아 있어 `GetTextFile`로는 보이므로 **텍스트 추출로 검증하면 못 잡는다.** [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- **`PageBreak` 속성 변경은 효과가 없었다.** HWPML 왕복으로 `Cell`·`Table`·`Division`·`Auto` 어느 값을 넣어도 결과가 같았다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- **해결은 표를 쪼개는 것.** `HAction.Run("TableSplitTable")`로 항목별 표로 분리하면 표 사이에서 페이지가 넘어간다. 개별 표가 한 쪽을 넘지 않으면 통째로 다음 쪽으로 밀려나며 잘리지 않는다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- **빈 셀은 찾기·바꾸기로 채울 수 없다.** 라벨 셀을 찾아 `TableRightCell`로 옆으로 이동해 넣는다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- **HWPML 왕복이 열려 있다.** `GetTextFile("HWPML2X")` → XML 문자열 치환 → `Open(path, "HWPML2X")`로 COM 프로퍼티에 노출되지 않은 문서 속성을 건드릴 수 있다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]
- **`SaveAs` 경로는 절대경로여야 한다.** 상대경로를 주면 오류 없이 다른 위치에 저장된다. [출처: sources/019-hwp-com-document-generation-2026-09-07.md]

## Details

### 서식 채우기 표준 절차

```
1) 빈 서식 .hwp 를 Open (HWP 포맷, 절대경로)
2) 항목 행마다 커서를 두고 TableSplitTable  ← 반드시 채우기 전에
3) 표 셀 채우기:  MoveDocBegin → RepeatFind(라벨) → Cancel → TableRightCell → InsertText
4) 라벨 뒤 본문:  RepeatFind(라벨) → Cancel → MoveLineEnd → InsertText  (문단 사이 BreakPara)
5) 본문 페이지:   MoveDocEnd → BreakPage → SetTextFile(html, "HTML", "insertfile")
6) SaveAs(hwp) + SaveAs(pdf) → PDF 렌더로 검증
```

2번을 3번보다 먼저 해야 한다. 내용을 다 채운 뒤 쪼개려 하면 이미 잘린 상태에서 시작한다.

### 삽입 전 문자 정리

```python
def cp949_safe(s):
    fallback = {"—": "―", "–": "-", "−": "-"}
    out = []
    for ch in s:
        try:
            ch.encode("cp949")
            out.append(ch)
        except UnicodeEncodeError:
            out.append(fallback.get(ch, "-"))
    return "".join(out)
```

### 검증 방법

PDF로 내보낸 뒤 세 가지를 본다.

| 확인 | 방법 | 잡히는 문제 |
|---|---|---|
| 페이지 수·페이지별 텍스트 길이 | PyMuPDF `get_text()` 길이 | 표 클리핑(특정 페이지가 비정상적으로 짧음) |
| `?` 개수 | 전체 텍스트에서 카운트 | CP949 문자 소실 |
| 실제 렌더 이미지 | `get_pixmap()` → PNG 확인 | 두부·레이아웃 붕괴 |

텍스트 추출만으로는 두부와 클리핑을 못 잡는다. **이미지 확인이 필수다.**

### 알려진 제약 (2026-08 확인분)

- `Open()`은 `.hwp`·`.html`·`.hwpml`만 True. **DOCX·RTF는 포맷 문자열을 무엇으로 줘도 False**
- HTML 필터는 **인라인 `style=` 속성만** 반영한다. `<style>` 블록의 클래스 규칙은 전부 무시
- HTML 필터가 무시하는 것: `page-break-before/after`, `bgcolor` 셀 음영, `cellpadding`

### 운영 함정

COM 호출 중 `Hwp.exe`를 강제 종료하면 다음 `Open()`이 `-2147023170`(원격 프로시저 호출 실패)로 죽는다. 대화상자를 띄운 채 멈추는 경우가 있어, 걸리면 프로세스를 정리하고 다시 시작한다.

## 함께 보기

- [[concept-powershell-regex-text-pitfalls]] — Windows 텍스트 처리에서 인코딩이 조용히 망가지는 다른 사례
