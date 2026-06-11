---
title: "Claude 4.x 신기능 & 하네스 적용"
wiki_type: topic
tags: [claude-4, adaptive-thinking, citations-api, routines, managed-agents, 1m-context]
last_modified_at: 2026-05-21
excerpt: "2026년 4월 기준 Claude 4.x 주요 신기능. Adaptive Thinking, Citations API, Routines, 1M Token Context 등 Henry 시스템 하네스 업그레이드에 직접 활용 가능한 기능 포함."
---

<span class="wiki-type-badge">topic</span>

## Summary
2026년 4월 기준 Claude 4.x 주요 신기능. Adaptive Thinking, Citations API, Routines, 1M Token Context 등 Henry 시스템 하네스 업그레이드에 직접 활용 가능한 기능 포함. [출처: sources/005-claude-4x-new-features.md]

## Key Facts
- **Adaptive Thinking**: 도구 호출 사이 추론 가능 (Interleaved Thinking) — Sonnet 4.6, Opus 4.7 [출처: 005]
- **Citations API**: 소스 문서 내 정확한 문장 자동 인용 — 전체 모델 [출처: 005]
- **Claude Code Routines**: 반복 작업 오프라인 스케줄링 자동화 [출처: 005]
- **1M Token Context (Beta)**: ~750,000단어 = ~2,500페이지 처리 — Sonnet 4.6, Opus 4.6 [출처: 005]
- **Managed Agents (Beta)**: 완전 관리형 에이전트 하네스, 보안 샌드박싱 포함 [출처: 005]

## Details

### 신기능 전체 목록

| 기능 | 모델 | Henry 적용 우선순위 |
|------|------|------------------|
| **Adaptive Thinking** | Sonnet 4.6, Opus 4.7 | 🟡 MEDIUM |
| **Citations API** | 전체 | 🟡 MEDIUM |
| **Claude Code Routines** | Claude Code | 🔴 HIGH |
| **1M Token Context (Beta)** | Sonnet 4.6, Opus 4.6 | 🟢 LOW |
| **Managed Agents (Beta)** | API | 🟢 LOW |
| **Agent Skills (Beta)** | Claude Code | 🟡 MEDIUM |
| **멀티세션 사이드바** | Claude Code | 🟡 MEDIUM |
| **Message Batches 300k** | Opus 4.6, Sonnet 4.6 | 🟢 LOW |

### 1. Routines → ms_specialist 자동화 [🔴 HIGH]
[출처: 005]
- **현황**: update-tracker-agent 수동 호출
- **적용**: Claude Code Routines로 매주 자동 실행
- 미완료 → 설정 파일 작성 필요

### 2. Citations API → research-agent + ms_specialist [🟡 MEDIUM]
[출처: 005]
- **현황**: URL만 나열, 인용 근거 없음
- **적용**: MS 공식 문서, Anthropic 릴리즈 노트에서 정확한 문장 인용
- 미완료 → research-agent 통합 필요

### 3. Interleaved Thinking → eda-agent + henry-orchestrator [🟡 MEDIUM]
[출처: 005]
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    thinking={"type": "enabled", "budget_tokens": 5000},
    ...
)
```
- **적용**: 분석 단계별 중간 추론 → 데이터 해석 오류 감소

### 4. 멀티세션 사이드바 → Fork-Join 시각화 [🟡 MEDIUM]
[출처: 005]
- henry-orchestrator 병렬 Agent 호출을 사이드바에서 모니터링
- 병렬 실행 워크플로우 정의서 작성 필요

### 5. 1M Token Context → ppt_team_agent + writing [🟢 LOW]
[출처: 005]
- 대용량 소스 문서를 단일 컨텍스트로 처리
- ppt-planner chunking 로직 단순화 가능

## Connections
- → [[Harness Engineering]] : 신기능이 하네스 설계에 미치는 영향
- → [[12 Agentic Harness Patterns]] : Routines = 패턴 #4 Dream Consolidation의 진화

## Open Questions
- Managed Agents (Beta): Henry 시스템이 자체 하네스를 유지할 가치가 있는가 vs. 완전 위임?
- Citations API 실제 연동 비용 측정 필요
