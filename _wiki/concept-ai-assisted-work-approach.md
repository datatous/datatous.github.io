---
title: "Henry의 AI 보조 업무 접근 방식"
wiki_type: concept
tags: [ai-workflow, report-writing, claude, methodology, copilot-poc]
last_modified_at: 2026-05-29
excerpt: "Henry는 AI(Claude)를 직접 결과물 생성 도구로 쓰기보다 **판단·정리·검증의 파트너**로 활용한다. PPT나 문서 작성 시 AI가 파일을 직접 수정하지 않고, 사람이 키인할 수 있는 정리된 텍스트를 제공하는 방식을 선호한다. 데이터는 항상 원본 소스와 대조 검증 후 확정한다."
---

<span class="wiki-type-badge">concept</span>

## Summary

Henry는 AI(Claude)를 직접 결과물 생성 도구로 쓰기보다 **판단·정리·검증의 파트너**로 활용한다. PPT나 문서 작성 시 AI가 파일을 직접 수정하지 않고, 사람이 키인할 수 있는 정리된 텍스트를 제공하는 방식을 선호한다. 데이터는 항상 원본 소스와 대조 검증 후 확정한다.

## Key Facts

- **보고서 작성 방식**: PPT 직접 편집 대신, 슬라이드 사진 업로드 → AI가 키인 텍스트 정리 → 사람이 직접 입력. AI는 편집 도구가 아닌 컨텐츠 정리 보조 역할. [출처: session-hanwha-ocean-report-2026-05-29]
- **데이터 검증 원칙**: 수치는 원본 데이터 파일(Excel, MD 총정리본)과 대조 확인 후 사용. 업데이트 일정(6/1 엑셀 재다운, 6/2 설문 마감)까지 중간 수치를 명시적으로 "현재 기준"으로 표시. [출처: session-hanwha-ocean-report-2026-05-29]
- **PDF 텍스트 추출 장벽 우회**: PowerPoint 생성 PDF는 CIDFont 인코딩 문제로 텍스트 추출 불가. PyMuPDF로 페이지를 PNG 이미지로 변환 후 Claude의 시각 인식으로 내용 추출하는 방식으로 해결. [출처: session-hanwha-ocean-report-2026-05-29]
- **툴 선택 기준 — 스킬 vs MCP**: MCP는 토큰 소비가 많아 부담. 같은 기능이면 skills.sh 스킬을 먼저 시도하고, 스킬이 없을 때 MCP를 고려. [출처: session-hanwha-ocean-report-2026-05-29]
- **다중 소스 교차 검증**: 시나리오명 확인 시 Draft MD + 최종 PDF를 모두 확인해 불일치 발견 ("답변 데이터" → "실적 데이터" 수정). 항상 최신 원본이 우선. [출처: session-hanwha-ocean-report-2026-05-29]
- **세션 로그 누적 저장**: 작업 결과를 `키인내용_세션로그.md` 같은 파일에 슬라이드별로 누적해 다음 세션에서도 이어서 사용할 수 있도록 관리. [출처: session-hanwha-ocean-report-2026-05-29]

## Details

### 보고서 작성 워크플로우

```
1. 사용자가 보고서 양식 사진 업로드
2. Claude: 레이아웃·텍스트 박스 분석
3. Claude: 키인할 텍스트 항목별로 정리 제공
4. 사용자: PPT에 직접 키인
5. 필요 시 재캡처로 확인
```

이 방식의 이점:
- PPT 파일 포맷 오염 위험 없음
- 사용자가 최종 품질 통제
- AI 오류를 사람이 필터링 가능

### PDF 한국어 텍스트 추출 문제

PowerPoint에서 생성된 한국어 PDF는 CIDFont에 ToUnicode 테이블이 없어 `pdftotext`, `pdfplumber`, `pdfminer` 모두 텍스트 추출 실패(깨진 문자 출력).

**해결 방법**: `PyMuPDF(fitz)`로 PDF 페이지 → PNG 변환 후 Claude 시각 인식으로 읽기.

```python
import fitz
doc = fitz.open("file.pdf")
page = doc[0]
mat = fitz.Matrix(2, 2)  # 2x 확대
clip = page.get_pixmap(matrix=mat)
clip.save("page1.png")
```

### 도구 우선순위

| 상황 | 우선 선택 | 이유 |
|---|---|---|
| 기능 확장 필요 | skills.sh 스킬 | 토큰 효율, 간단한 설치 |
| 스킬 없는 전문 기능 | MCP | 토큰 많이 소비하지만 기능 강력 |
| 데이터 분석 | Python 직접 실행 | 정확하고 빠름 |

### MCP 설치 방법 (kordoc 사례)

`settings.json`의 `mcpServers` 필드는 유효하지 않음. 올바른 방법:
- 사용자 레벨: `C:\Users\{user}\.claude\.mcp.json`
- 프로젝트 레벨: `{project-root}\.mcp.json`

```json
{
  "mcpServers": {
    "kordoc": {
      "command": "npx",
      "args": ["-y", "kordoc", "mcp"]
    }
  }
}
```

## Connections

- → [[Harness Engineering]] : AI 도구 활용 방식은 전반적인 하네스 설계 철학과 연결
- → [[skills.sh]] : 스킬 우선 접근의 구체적 생태계

## Open Questions

- kordoc MCP가 실제로 한국어 PDF 텍스트 추출에 효과적인지 검증 필요 (현 세션에서 `.mcp.json` 생성 후 재시작 필요)
- PyMuPDF 시각 접근 방식과 kordoc MCP 방식의 정확도 비교
