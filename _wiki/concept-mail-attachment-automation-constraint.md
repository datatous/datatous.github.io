---
title: "메일 첨부파일 자동화의 MCP 제약과 우회 경로"
wiki_type: concept
tags: [gmail, mcp, apps-script, automation, google-drive, personal-data-pipeline]
last_modified_at: 2026-07-21
excerpt: "claude.ai Gmail MCP는 메일 첨부파일의 메타데이터만 제공하고 본체 다운로드를 지원하지 않는다. '메일 첨부 → 자동 처리'가 필요한 워크플로우는 예외 없이 Google Apps Script (또는 수동 저장)로 Gmail과 Drive 사이를 잇는 우회 경로를 전제로 설계해야 한다."
---

<span class="wiki-type-badge">concept</span>

## Summary

claude.ai Gmail MCP는 메일 첨부파일의 메타데이터만 제공하고 본체 다운로드를 지원하지
않는다. "메일 첨부 → 자동 처리"가 필요한 워크플로우는 예외 없이 Google Apps Script
(또는 수동 저장)로 Gmail과 Drive 사이를 잇는 우회 경로를 전제로 설계해야 한다.

## Key Facts

- Gmail MCP `get_message`는 첨부파일 메타데이터(파일명, 크기 등)만 반환하고 첨부
  파일 본체는 가져오지 못한다. [출처: sources/009-personal-data-automation-api-constraints.md]
- 우회 경로: Google Apps Script를 시간 기반 트리거로 등록 → Gmail 첨부를 Drive
  폴더에 저장. [출처: sources/009-personal-data-automation-api-constraints.md]
- xlsx 등 오피스 포맷은 Drive 상에서 Google Sheet로 변환(`Drive.Files.copy` +
  `MimeType.GOOGLE_SHEETS`)해 둬야 Drive MCP `read_file_content`로 바로 읽을 수
  있다. 변환 없이 두면 매번 로컬 다운로드 + 별도 파싱(openpyxl 등)이 필요하다.
  [출처: sources/009-personal-data-automation-api-constraints.md]
- 이 제약은 특정 발신자에 한정되지 않고 Gmail MCP로 받는 모든 첨부파일 자동화에
  공통 적용된다. [출처: sources/009-personal-data-automation-api-constraints.md]

## Details

### 왜 첨부 자동화가 막히는가

Gmail MCP가 첨부 다운로드를 지원하지 않는 것은 도구 자체의 스키마 제약이다. 메일
본문 텍스트는 읽을 수 있어도 첨부된 바이너리(xlsx, pdf, csv 등)에는 접근 경로가
없다. 이 제약을 파악하지 않고 "메일에서 파일 받아서 자동 처리"를 설계하면 초반
구현 단계에서 막힌다.

### 공통 패턴 — Apps Script 브리지

1. Apps Script 시간 트리거(`GmailApp.search` 등)로 조건에 맞는 메일을 스캔
2. 첨부파일을 `DriveApp` 폴더에 저장
3. 필요 시 포맷 변환 (예: xlsx → Google Sheet)
4. Drive MCP `read_file_content`로 후속 처리

이 패턴은 특정 서비스에 국한되지 않고 "메일로만 받을 수 있는 파일을 에이전트가
읽어야 하는" 모든 케이스에 적용 가능한 범용 우회 경로다.

### 관련 사례 — 개인 데이터 내보내기 소스의 형식 제약 (일반 사실)

메일 첨부 경로가 필요한 소스는 대개 공식 조회 API가 없어 "내보내기 → 이메일
수신"만 지원하는 경우다. 예: 가계부류 앱은 개인용 조회 API가 없고(마이데이터
API는 사업자 전용 인가제), 앱 내 내보내기 기능으로 최근 일정 기간치 xlsx만
이메일로 받을 수 있는 경우가 흔하다. 이런 소스는 기간 지정이 불가한 경우가 많아,
히스토리를 쌓으려면 정기 스냅샷을 누적하고 지문(fingerprint) 기반으로 중복
제거하는 설계가 필요하다. [출처: sources/009-personal-data-automation-api-constraints.md]

메신저류(대화 조회 API가 아예 없는 경우)는 이 패턴과 별개로, 공식 "대화
내보내기(.txt)" 기능을 통해서만 데이터를 얻을 수 있다. PC 로컬 데이터가
존재하더라도 기기 종속 암호화가 걸려 있어 범용 복호화 경로로 삼기 어렵다.
[출처: sources/009-personal-data-automation-api-constraints.md]

## Connections

- → [[Henry Agentic System]] : 이 제약을 우회한 개인 데이터 파이프라인이 궁극적으로
  참조하게 될 하네스. 단, 지식층을 llm_wiki에 통합할지는 공개 동기화 제약(같은 페이지
  참조)과 별도로 결정해야 한다.

## Open Questions

- Apps Script 설치 여부, 화이트리스트 대상 등 실제 파이프라인 구현은 Henry 컨펌
  대기 상태 (2026-07-21 기준 미착수)
- 개인 데이터 지식층 저장 위치(별도 저장소 vs llm_wiki 통합+가드)는 미결 — 결정되면
  이 페이지 및 [[Henry Agentic System]] 페이지 갱신 필요
