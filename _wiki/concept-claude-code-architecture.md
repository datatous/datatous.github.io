---
title: "Claude Code Architecture"
wiki_type: concept
tags: [claude-code, permissions, compaction, harness, architecture]
last_modified_at: 2026-05-30
excerpt: "Claude Code는 CLI 기반 AI 코딩 에이전트로, 모델(Model)과 하네스(Harness)가 분리된 권한 아키텍처를 사용한다. 모델이 무엇을 할지 결정하고, 별도 시스템이 허용 여부를 결정하는 책임 분리가 핵심 설계 원칙이다."
---

<span class="wiki-type-badge">concept</span>

## Summary
Claude Code는 CLI 기반 AI 코딩 에이전트로, 모델(Model)과 하네스(Harness)가 분리된 권한 아키텍처를 사용한다. 모델이 무엇을 할지 결정하고, 별도 시스템이 허용 여부를 결정하는 책임 분리가 핵심 설계 원칙이다. [출처: sources/003-wavespeed-claude-arch.md]

## Key Facts
- **책임 분리**: 모델의 실행 결정 ≠ 하네스의 허용 결정 — 두 레이어가 독립적으로 동작 [출처: 003]
- **백그라운드 분류기**: 사용자 의도 + 도구 호출을 감시하되, 모델 내부 추론은 의도적으로 제외 (설득 공격 방지) [출처: 003]
- **자동 컴팩션**: 컨텍스트 ~98% 도달 시 자동 실행. Full context reset이 compaction보다 충실도 높은 경우도 존재 [출처: 003]
- **MCP Lazy Tool Discovery**: 도구 이름만 초기 로드, 스키마는 필요 시 동적 발견 — 컨텍스트 효율화 [출처: 003]
- **MCP 서버 권장 상한**: 5~6개 (서브프로세스 오버헤드 고려) [출처: 003]

## Details

### 권한 3단계
[출처: 003]

| 단계 | 동작 | 예시 |
|------|------|------|
| Auto-approved | 자동 허용 | 읽기 전용 작업 |
| Prompt for confirmation | 사용자 승인 요청 | 파일 수정, 상태 변경 |
| Require explicit approval | 명시적 허가 필수 | 고위험 작업 (삭제, push 등) |

### 컨텍스트 관리
- 컴팩션: 자동(~98%) 또는 수동(`/compact`)
- 중요 세션에서는 `/clear` 후 재시작이 compaction보다 더 정확한 컨텍스트 제공 가능
- `CLAUDE.md` 파일로 프로젝트 컨텍스트 영구화

### settings.json 권한 구조
```json
{
  "permissions": {
    "allow": ["Bash(git *)", "Read(**)"],
    "deny": ["Bash(rm -rf *)"]
  }
}
```
- allow → ask → deny 순서 적용 (deny-first 파이프라인)

## Connections
- → [[Harness Engineering]] : 권한 아키텍처가 속한 상위 패러다임
- → [[12 Agentic Harness Patterns]] : 실제 구현 패턴 목록
- → [[Henry Agentic System]] : Henry의 Claude Code 기반 구현체

## Open Questions
- Extended session에서 compaction vs. full reset 선택 기준 가이드라인 미수립
- MCP 서버 5~6개 초과 시 실질적 성능 저하 임계점 데이터 없음
