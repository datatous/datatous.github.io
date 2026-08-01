---
title: "텍스트 처리 함정 — PowerShell BOM과 정규식 \\s"
wiki_type: concept
tags: [powershell, regex, encoding, windows, gotcha]
last_modified_at: 2026-07-31
excerpt: "텍스트/스크립트를 다루다 반복적으로 재발할 수 있는 두 가지 함정 — ① PowerShell 5.1의 BOM 없는 스크립트 인코딩 오독, ② 정규식 `\\s`가 개행을 포함해 줄 단위 정제 시 다음 줄을 통째로 삼키는 문제. 음성 출력용 텍스트 정제 스크립트를 만드는 과정에서 둘 다 실제로 발생했다."
---

<span class="wiki-type-badge">concept</span>

## Summary
텍스트/스크립트를 다루다 반복적으로 재발할 수 있는 두 가지 함정 —
① PowerShell 5.1의 BOM 없는 스크립트 인코딩 오독, ② 정규식 `\s`가 개행을
포함해 줄 단위 정제 시 다음 줄을 통째로 삼키는 문제. 음성 출력용 텍스트
정제 스크립트를 만드는 과정에서 둘 다 실제로 발생했다.
[출처: sources/013-voice-control-mcp-2026-07-31.md]

## Key Facts
- **PowerShell 5.1은 BOM 없는 `.ps1`을 ANSI(한국어 환경에서는 cp949)로
  읽는다** — UTF-8 no-BOM으로 저장된 스크립트 안의 한글 리터럴이 깨진
  문자로 실행된다 [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **진단 단서**: 외부 입력(stdin, 파일 등)으로 들어온 한글은 정상인데,
  **스크립트 파일 안에 직접 적힌 한글 리터럴만** 깨진다는 비대칭이
  나타난다 [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **해결**: 스크립트를 UTF-8 **with BOM**으로 저장. 에디터/자동화 도구의
  기본 저장 인코딩이 UTF-8 no-BOM인 경우가 많아 재발 위험이 높다
  [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **정규식 `\s`는 스페이스·탭뿐 아니라 개행 문자도 포함한다** — 줄 단위
  정제 패턴(`^\s{4,}\S.*$` 등)에 쓰면 빈 줄 + 다음 줄의 선행 공백이
  이어지며 의도치 않게 멀쩡한 다음 줄 전체를 매칭·삭제할 수 있다
  [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **해결**: 줄 내부 공백만 노릴 때는 `\s` 대신 `[ \t]`를 사용한다
  (`[ \t]{4,}`) [출처: sources/013-voice-control-mcp-2026-07-31.md]

## Details

### 재발 조건
- BOM 함정: 코드 생성 도구·에디터가 파일을 새로 쓸 때, 특히 자동화된
  Write 동작에서 UTF-8 no-BOM이 기본값인 경우가 흔하다. `.ps1` 파일에
  한글(또는 비ASCII) 리터럴이 포함되는 모든 케이스에서 재발 가능.
- 정규식 함정: 마크다운/텍스트 정제, 로그 필터링 등 "들여쓴 블록 제거",
  "특정 패턴의 줄 삭제" 류 작업에서 `\s`를 개행 미포함으로 착각하고
  쓰는 모든 언어(PowerShell, Python, JS 등)에서 동일하게 재발 가능 —
  PowerShell 한정 문제가 아니다.

### 실제 증상
- BOM 문제: `"$n 번."` 이 `1 踰?` 처럼 깨진 문자로 음성 출력됨.
- 정규식 문제: 정상적인 문장 한 줄이 정제 후 통째로 사라짐.

## Connections
- → [[로컬 음성 에이전트 파이프라인 구성 패턴 (Windows)]] : 두 함정 모두
  이 파이프라인의 텍스트 정제 스크립트 구현 중 발견됨

## Open Questions
- 다른 셸(PowerShell 7+/pwsh)에서도 동일한 BOM 오독이 재현되는지 미검증
  (5.1 한정 가능성)
