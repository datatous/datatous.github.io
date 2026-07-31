---
title: "로컬 음성 에이전트 파이프라인 구성 패턴 (Windows)"
wiki_type: concept
tags: [voice, mcp, stt, tts, faster-whisper, windows, local-first]
last_modified_at: 2026-07-31
excerpt: "API 키·클라우드 비용 없이 Windows에서 로컬로 완결되는 음성 대화(말하기↔듣기) 파이프라인 구성 패턴. faster-whisper 로컬 STT + Windows 내장 SAPI TTS + 침묵 감지 기반 자동 종료 + 병렬 발화 직렬화로 구성한다. Claude Code의 네이티브 음성 슬래시 명령이 환경에서 막혀 있을 때, MCP 도구로 같은 기능을"
---

<span class="wiki-type-badge">concept</span>

## Summary
API 키·클라우드 비용 없이 Windows에서 로컬로 완결되는 음성 대화(말하기↔듣기)
파이프라인 구성 패턴. faster-whisper 로컬 STT + Windows 내장 SAPI TTS +
침묵 감지 기반 자동 종료 + 병렬 발화 직렬화로 구성한다. Claude Code의
네이티브 음성 슬래시 명령이 환경에서 막혀 있을 때, MCP 도구로 같은 기능을
직접 구현해 우회한 사례에서 도출됐다. [출처: sources/013-voice-control-mcp-2026-07-31.md]

## Key Facts
- **STT**: `faster-whisper` `small` 모델, CPU int8, 완전 로컬 실행. API 키
  불필요, 한국어 인식 품질 실사용 가능 수준. 최초 1회 모델 다운로드 후
  캐시, 최초 로드 약 18초 [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **TTS**: Windows 내장 SAPI(`System.Speech`)의 한국어 음성을 재사용 —
  추가 설치·API 불필요 [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **녹음 종료 판정**: 키 입력이 아니라 RMS(음량) 기반 침묵 감지 — 임계값
  이하가 일정 시간(예: 1500ms) 지속되면 자동 종료. 실측 환경 소음 RMS
  21 / 임계값 450 (여유 충분) [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **병렬 발화 겹침 방지**: 전역 named mutex로 TTS 발화를 직렬화. 동시에
  끝난 요청은 뒤엣것이 대기 후 순차 재생, 일정 시간(예: 60초) 초과 대기는
  폐기 [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **비용**: 0원 (STT·TTS 모두 로컬, 벤더 록인 없음)
  [출처: sources/013-voice-control-mcp-2026-07-31.md]

## Details

### 도구 인터페이스 설계
대화형 루프를 MCP 도구로 노출할 때 아래 4개로 나누면 자연스럽게 구성된다.
[출처: sources/013-voice-control-mcp-2026-07-31.md]

| 도구 | 역할 |
|------|------|
| `converse(text)` | 말하고 → 듣고 → 텍스트 반환 (대화 한 턴) |
| `listen()` | 듣기만, 침묵 감지 시 종료 |
| `say(text)` | 말하기만 |
| `calibrate()` | 방 소음 측정 — 인식 이상 시 임계값 점검용 |

### 텍스트 정제 (TTS 앞단)
답변 텍스트를 그대로 읽으면 마크다운·코드블록·URL·이모지까지 낭독되는
문제가 생긴다. TTS로 넘기기 전에 이를 걷어내고 문장 경계에서 길이를
절단(예: 180자)하는 정제 단계를 넣는다. [출처: sources/013-voice-control-mcp-2026-07-31.md]

### 조정 가능한 파라미터
모델 크기(정확도↔속도 트레이드오프), 언어, 침묵 판정 시간, 소음 임계값은
환경변수나 스크립트 상단 상수로 노출해 두면 환경별로 튜닝하기 쉽다.
[출처: sources/013-voice-control-mcp-2026-07-31.md]

### 시도했으나 폐기한 경로 (재시도 방지)
- **오픈소스 음성 MCP 프로젝트의 Windows 네이티브 설치**: 오디오 재생
  의존 패키지가 2019년 이후 릴리스가 끊겨 Python 3.11용 사전 빌드 휠이
  없음. 빌드하려면 MSVC Build Tools(수 GB) 필요 → 직접 구현으로 전환.
  WSL 경유도 오디오 패스스루 + 한국어 TTS 지원이 둘 다 불확실해 기각
  [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **CLI 전용 메신저 채널 브릿지**: 별도 플래그로 CLI를 기동해야 활성화되는
  구조라, 여러 탭을 병렬로 쓰는 워크플로우와 대화 맥락이 분리되어 실익이
  적음 [출처: sources/013-voice-control-mcp-2026-07-31.md]
- **모바일 앱의 양방향 음성 모드**: 코딩 에이전트 환경에서는 공식적으로
  미지원, 일반 채팅 탭 전용. 원격 제어 경로의 음성 지원은 이 시점 기준
  아직 요청 단계 [출처: sources/013-voice-control-mcp-2026-07-31.md]

## Connections
- → [[Claude Code Architecture]] : 슬래시 명령이 막혀도 MCP 도구는 별도
  레이어로 작동한다는 우회 원리와 연결
- → [[Henry Agentic System]] : 하네스에 음성 입출력 도구가 추가된 확장 사례
- → [[텍스트 처리 함정 — PowerShell BOM과 정규식 \s]] : 같은 작업에서
  함께 발견된 구현 함정

## Open Questions
- 침묵 감지 임계값(RMS/지속시간)이 다른 환경(소음이 큰 공간 등)에서도
  안정적인지 미검증 — 현재는 단일 환경 실측치만 있음
- `medium` 모델로 전환 시 정확도 개선 폭과 지연 시간 트레이드오프 미측정
