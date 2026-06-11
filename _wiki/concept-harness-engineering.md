---
title: "Harness Engineering"
wiki_type: concept
tags: [harness, architecture, kv-cache, defense, context-engineering]
last_modified_at: 2026-05-21
excerpt: "AI 개발 패러다임의 3세대. Agent = Model + Harness 공식으로, 하네스가 OS 역할을 수행한다. KV-cache hit rate가 프롬프트 품질을 대체하는 핵심 최적화 지표."
---

<span class="wiki-type-badge">concept</span>

## Summary
AI 개발 패러다임의 3세대. Agent = Model + Harness 공식으로, 하네스가 OS 역할을 수행한다. KV-cache hit rate가 프롬프트 품질을 대체하는 핵심 최적화 지표. [출처: sources/001-harness-bits-bytes.md]

## Key Facts
- **패러다임 진화**: Prompt Engineering(2022-24) → Context Engineering(2025) → Harness Engineering(2026+) [출처: 001]
- **하네스 구성**: 컨텍스트 큐레이션 + 도구 관리 + 권한 제어 + 오류 복구 [출처: 001]
- **KV-cache**: prefix 안정화로 최대 10x 비용 절감 가능 — 에이전트 파일 섹션 순서가 캐시 히트율 결정 [출처: 001]
- **도구 권한 3단계**: Auto-approved(읽기 전용) → Prompt for confirmation(상태 변경) → Require explicit approval(고위험) [출처: 003]
- **deny-first 파이프라인**: allow → ask → deny 순서 규칙 적용 [출처: 003]

## Details

### 4-Quadrant Defense Framework
[출처: 001]

|  | Feedforward (예방) | Feedback (교정) |
|---|---|---|
| **Deterministic** | Guides (CLAUDE.md, rules) | Computational (linters, hooks) |
| **Non-Deterministic** | System prompts (role, constraints) | Inferential (LLM-as-judge) |

효과적인 하네스는 4개 방어를 모두 레이어링한다.

### Ralph Pattern (중간자 패턴)
[출처: 001]
- 에이전트가 직접 실행 대신 계획 → 승인 → 실행 3단계 분리
- 고위험 작업에서 Human-in-the-loop 보장

### Lethal Trifecta (보안 격리)
[출처: 001]
비신뢰 입력을 처리하는 에이전트는 3가지 권한을 의도적으로 미보유:
1. Write 권한 없음
2. Edit 권한 없음
3. Bash 실행 없음
→ Henry 시스템 `research-agent`에 구현됨

### KV-Cache 섹션 순서 규약
[출처: 001, Henry 시스템 v6.0]
```
1. frontmatter       ← 안정적 prefix (캐시 대상)
2. Role/목표
3. Workflow/Rules
4. Output Format
── KV-cache hit boundary ──
5. Learned Rules     ← append-only
6. Session Memory    ← 매 세션 변경
```

### Claude Code 권한 아키텍처
[출처: 003]
- 모델이 무엇을 할지 결정 ≠ 다른 시스템이 허용 여부 결정 (책임 분리)
- 백그라운드 분류기: 사용자 의도 + 도구 호출 보임, 모델 추론 의도적 제외 (설득 공격 방지)
- MCP 서버 권장 상한: 5-6개 (서브프로세스 오버헤드)

### 컨텍스트 관리
[출처: 003]
- 컨텍스트 ~98% 시 자동 컴팩션
- **핵심**: Extended session에서 full context reset이 compaction보다 충실도 높은 경우 있음
- MCP Lazy Tool Discovery: 이름만 초기 로드, 스키마는 필요 시 동적 발견

## Connections
- → [[12 Agentic Harness Patterns]] : 이 개념의 구체적 구현 패턴 목록
- → [[Claude Code Architecture]] : 권한/컴팩션 상세 구현
- → [[Henry Agentic System]] : Henry의 하네스 구현체

## Open Questions
- Full context reset 전략: extended session 시 언제 reset할지 가이드라인 미수립
- 토큰 버짓 모니터링: 컨텍스트 사용량 가시화 도구 없음
