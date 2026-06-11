---
title: "skills.sh"
wiki_type: entity
tags: [skills, ecosystem, modular, npx, community]
last_modified_at: 2026-05-21
excerpt: "Claude Code, GitHub Copilot, Cursor, Cline, Gemini 등 다양한 에이전트 플랫폼에서 사용 가능한 재사용 스킬 마켓플레이스. `npx skills add <owner/repo>`로 설치."
---

<span class="wiki-type-badge">entity</span>

## Summary
Claude Code, GitHub Copilot, Cursor, Cline, Gemini 등 다양한 에이전트 플랫폼에서 사용 가능한 재사용 스킬 마켓플레이스. `npx skills add <owner/repo>`로 설치. [출처: sources/004-skills-sh.md]

## Key Facts
- **총 설치 수**: 91,000+ | 등록 스킬: 246+ [출처: 004]
- **주요 공급자**: `vercel-labs/agent-skills`, `anthropics/skills`, `microsoft/azure-skills` [출처: 004]
- **설치 명령**: `npx skills add <owner/repo>` — 프레임워크 무관 [출처: 004]
- **Henry 시스템 연관**: `.claude/skills/` 구조가 유사하나 내부 전용 [출처: 004]

## Details

### 핵심 개념
- **Skills = Modular Procedural Knowledge**: 에이전트가 설치하여 전문 지식과 절차를 얻는 재사용 가능한 단위
- 프레임워크 무관 (Claude Code, Copilot, Cursor 등 지원)

### 주요 커맨드
```bash
npx skills find [query]     # 스킬 검색
npx skills add <owner/repo> # 설치
npx skills check            # 업데이트 확인
npx skills update           # 전체 업데이트
```

### Henry 시스템 현황 비교
| 기능 | skills.sh | Henry 시스템 |
|------|----------|------------|
| 스킬 구조 | owner/repo@skill | `.claude/skills/*/SKILL.md` |
| 범위 | 공개 마켓플레이스 | 내부 전용 |
| 설치 방식 | npx 자동 | 수동 생성 |
| 공유 범위 | 글로벌 | 루트 + 워커별 |

### 향후 고려 사항 [출처: 004]
- 스킬 컴포저빌리티 (스킬이 스킬 호출) — 미구현
- 스킬 버전 필드 추가 가능
- 커뮤니티 스킬 설치 (`npx skills add anthropics/...`)

## Connections
- → [[12 Agentic Harness Patterns]] : 패턴 #10 Modular Skill Pattern의 커뮤니티 구현
- → [[Harness Engineering]] : 스킬 생태계의 이론적 맥락

## Open Questions
- Henry 시스템에서 `skills.sh`의 공개 스킬을 선별 도입할 만한 후보 발굴 필요
