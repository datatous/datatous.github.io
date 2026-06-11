---
title: "Henry Agentic System"
wiki_type: entity
tags: [agentic-system, harness, orchestrator, workers, henry]
last_modified_at: 2026-05-30
excerpt: "오현근(Henry)이 설계·운영하는 Claude Code 기반 멀티 에이전트 시스템. Orchestrator + Worker 패턴으로 도메인별 워커 노드가 분리된 구조이며, 메모리·스킬·라우팅 테이블이 하네스 레이어에서 관리된다."
---

<span class="wiki-type-badge">entity</span>

## Summary
오현근(Henry)이 설계·운영하는 Claude Code 기반 멀티 에이전트 시스템. Orchestrator + Worker 패턴으로 도메인별 워커 노드가 분리된 구조이며, 메모리·스킬·라우팅 테이블이 하네스 레이어에서 관리된다.

## Key Facts
- **루트 경로**: `c:\Users\Henry\Desktop\dev\`
- **진입점**: `CLAUDE.md` (라우팅 테이블 정의)
- **오케스트레이터**: `henry-orchestrator` — 복합 도메인 작업 조율
- **워커 노드**: 도메인별 폴더 (writing/, ppt_team_agent/, data_analysis/ 등)
- **메모리 시스템**: `C:\Users\Henry\.claude\projects\...\memory\` — 4가지 타입 (user/feedback/project/reference)
- **스킬**: `.claude/skills/` — 재사용 가능한 루틴 (save-log, analyze-me 등)

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

## Connections
- → [[Harness Engineering]] : 시스템이 구현하는 패러다임
- → [[12 Agentic Harness Patterns]] : 구현된 패턴 목록
- → [[Claude Code Architecture]] : 기반 아키텍처

## Open Questions
- 워커 간 output → input 파이프라인 자동화 미완성
- 토큰 사용량 모니터링 대시보드 없음
