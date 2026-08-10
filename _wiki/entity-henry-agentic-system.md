---
title: "Henry Agentic System"
wiki_type: entity
tags: [agentic-system, harness, orchestrator, workers, henry]
last_modified_at: 2026-07-31
excerpt: "오현근(Henry)이 설계·운영하는 Claude Code 기반 멀티 에이전트 시스템. Orchestrator + Worker 패턴으로 도메인별 워커 노드가 분리된 구조이며, 메모리·스킬·라우팅 테이블이 하네스 레이어에서 관리된다."
---

<span class="wiki-type-badge">entity</span>

## Summary
오현근(Henry)이 설계·운영하는 Claude Code 기반 멀티 에이전트 시스템. Orchestrator + Worker 패턴으로 도메인별 워커 노드가 분리된 구조이며, 메모리·스킬·라우팅 테이블이 하네스 레이어에서 관리된다.

## Key Facts
- **루트 경로**: 로컬 개발 리포 (경로는 머신마다 다름 — 리포 내 참조는 루트 기준 상대경로 사용)
- **진입점**: `CLAUDE.md` (라우팅 테이블 정의)
- **오케스트레이터**: `henry-orchestrator` — 복합 도메인 작업 조율
- **워커 노드**: 도메인별 폴더 (writing/, ppt_team_agent/, data_analysis/ 등)
- **메모리 시스템**: 사용자 홈의 `.claude/projects/<프로젝트>/memory/` — 4가지 타입 (user/feedback/project/reference)
- **스킬**: `.claude/skills/` — 재사용 가능한 루틴 (save-log, analyze-me 등)
- **⚠️ 위키 공개 동기화**: `tools/blog_sync/wiki_to_blog.py`는 `llm_wiki/wiki/pages/*.md`
  전체를 제외 필터 없이 datatous.github.io로 동기화한다 — exclude/private 조건이
  코드에 없음(2026-07-21 확인). `wiki/pages/`에 넣는 파일은 다음 동기화 실행 시
  전부 공개된다는 뜻이므로, 비공개 성격 자료는 애초에 wiki에 넣지 않아야 한다.
  [출처: sources/009-personal-data-automation-api-constraints.md]
- **음성 입출력 도구 추가**: 하네스에 로컬 음성 대화 MCP 도구(말하기·듣기·
  대화 한 턴·소음 보정)와 답변 자동 낭독 훅을 추가했다. 네이티브 슬래시
  음성 명령이 막혀 있던 환경에서 MCP 도구로 우회 구현한 사례
  [출처: sources/013-voice-control-mcp-2026-07-31.md]

## Details

### 라우팅 테이블 (주요 노드)

| 도메인 | 워커 | 에이전트 |
|--------|------|---------|
| PPT, 발표 | ppt_team_agent/ | ppt-planner → ppt-builder |
| 블로그, 포트폴리오 | writing/ | write-for-me |
| 보고서, 제안서 | writing/ | write-for-company |
| 데이터, 분석, EDA | data_analysis/ | eda-agent |
| M365, Power Platform | ms_specialist/ | update-tracker-agent |
| Wiki, 지식베이스 | llm_wiki/ | wiki-ingest/query/lint |
| Google Drive 정리 | gdrive_organizer/ | gdrive-organizer |
| 일일 업무 브리핑 | daily_brief/ | daily-brief |
| 석사 논문 | thesis/ | thesis-advisor |

### 메모리 4-레이어

| 레이어 | 내용 |
|--------|------|
| user | Henry 프로필, 선호도, 역할 |
| feedback | 과거 교정·확인된 접근방식 |
| project | 진행 중 프로젝트 현황 |
| reference | 외부 시스템 포인터 |

### 핵심 스킬
- `save-log` — 세션 작업 로그 저장
- `analyze-me` — work_logs 패턴 분석
- `daily-brief` — 일일 업무 브리핑 생성
- `status` — 전체 워커 현황 조회

### 블로그 동기화 메커니즘 (llm_wiki → 공개 위키)

`tools/blog_sync/wiki_to_blog.py`가 `llm_wiki/wiki/pages/*.md`를 읽어
datatous.github.io의 `_wiki/` 콘텐츠로 변환·배포한다. 2026-07-21 기준 스크립트에는
페이지 단위 제외 조건(예: frontmatter `visibility: private`)이 없어 **전량 무필터
동기화**된다. 비공개 자료를 wiki에 통합하려면 이 스크립트에 스킵 조건을 먼저
추가해야 하며, 그 전까지는 wiki에 넣은 모든 페이지가 공개 대상이라고 가정해야
한다. [출처: sources/009-personal-data-automation-api-constraints.md]

## Connections
- → [[Harness Engineering]] : 시스템이 구현하는 패러다임
- → [[12 Agentic Harness Patterns]] : 구현된 패턴 목록
- → [[Claude Code Architecture]] : 기반 아키텍처
- → [[메일 첨부파일 자동화의 MCP 제약과 우회 경로]] : 개인 데이터 파이프라인을 이
  하네스에 통합할 때 함께 고려해야 할 공개 동기화 제약
- → [[로컬 음성 에이전트 파이프라인 구성 패턴 (Windows)]] : 하네스에 추가된
  음성 입출력 확장

## Open Questions
- 워커 간 output → input 파이프라인 자동화 미완성
- 토큰 사용량 모니터링 대시보드 없음
- `wiki_to_blog.py`에 `visibility: private` 스킵 조건을 추가할지, 아니면 비공개
  지식은 애초에 llm_wiki 밖(별도 저장소)에 둘지 미결 (2026-07-21 기준)
