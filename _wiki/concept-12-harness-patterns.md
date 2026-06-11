---
title: "12 Agentic Harness Patterns"
wiki_type: concept
tags: [harness, patterns, memory, orchestration, hooks, dream-consolidation, tiered-memory]
last_modified_at: 2026-05-21
excerpt: "Claude Code 기반 에이전틱 하네스에서 검증된 12개 설계 패턴. 메모리·컨텍스트·보안·오케스트레이션 4개 범주로 구성."
---

<span class="wiki-type-badge">concept</span>

## Summary
Claude Code 기반 에이전틱 하네스에서 검증된 12개 설계 패턴. 메모리·컨텍스트·보안·오케스트레이션 4개 범주로 구성. [출처: sources/002-harness-12-patterns.md]

## Key Facts
- **#3 Tiered Memory**: 항상 로드(인덱스 200줄) / 온디맨드(주제별) / 검색(전체 기록) 3계층 [출처: 002]
- **#4 Dream Consolidation**: 백그라운드에서 메모리 정리·재구성, 중복 제거 [출처: 002]
- **#1 Persistent Instruction File**: CLAUDE.md로 구현 — 세션마다 자동 로드 [출처: 002]
- **#2 Scoped Context Assembly**: 계층적 파일 로딩, `.claude/rules/`로 구현 [출처: 002]

## Details

### 메모리 & 컨텍스트 패턴

**#1 Persistent Instruction File Pattern**
- 빌드 명령, 아키텍처 규칙, 네이밍 컨벤션 정의
- → **Henry 시스템**: CLAUDE.md ✅

**#2 Scoped Context Assembly Pattern**
- 코드베이스 위치에 따라 다른 규칙 적용
- → **Henry 시스템**: `writing/.claude/rules/`, `data_analysis/.claude/rules/` ✅

**#3 Tiered Memory Pattern**
- 항상 로드: 컴팩트 인덱스 (200줄 cap)
- 온디맨드: 주제별 파일
- 필요 시 검색: 전체 세션 기록
- → **Henry 시스템**: MEMORY.md + `memory/` 구조 ✅ (200줄 cap 준수 필요)

**#4 Dream Consolidation Pattern**
- 백그라운드 프로세스가 주기적으로 메모리 정리/재구성
- → **Henry 시스템**: `/consolidate-memory` 스킬 ✅ (v6.0 추가)

**#5 Progressive Context Compaction Pattern**
- 최근 턴 상세 유지, 오래된 것 요약
- → **Henry 시스템**: 부분 구현

### 보안 패턴

**#6 Lethal Trifecta Isolation**
- 비신뢰 입력 처리 에이전트 = Write/Edit/Bash 의도적 미보유
- → **Henry 시스템**: `research-agent` ✅

**#7 Deny-First Permission Pipeline**
- allow → ask → deny 순서
- → **Henry 시스템**: PreToolUse 훅 ✅

### 오케스트레이션 패턴

**#8 Fork-Join Parallelism**
- 독립 서브태스크 병렬 Agent 호출
- → **Henry 시스템**: `henry-orchestrator` 병렬 실행 ✅

**#9 Ralph Pattern (Human-in-the-Loop)**
- 고위험 작업: 계획 → 승인 → 실행
- → **Henry 시스템**: church-poster 등 게시 전 Henry 확인 필수 ✅

### 도구 & 스킬 패턴

**#10 Modular Skill Pattern**
- 재사용 가능한 절차를 스킬로 패키징
- → **Henry 시스템**: `.claude/skills/` ✅

**#11 Shared vs. Local Skill Promotion**
- 2+ 워커 사용 스킬 → 루트 승급
- → **Henry 시스템**: `report-skill`, `review-skill` 등 루트 공유 ✅

**#12 Background Agent Pattern**
- 장시간 실행: `background: true`
- → **Henry 시스템**: eda-agent, update-tracker-agent, ppt-builder ✅

## Connections
- → [[Harness Engineering]] : 이 패턴들의 이론적 기반
- → [[skills.sh]] : 패턴 #10, #11의 커뮤니티 구현체

## Open Questions
- 패턴 #5 Progressive Compaction: Henry 시스템에서 명확한 구현 방안 미정
