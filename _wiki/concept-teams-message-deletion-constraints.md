---
title: "Teams 메시지 삭제의 구조적 제약"
wiki_type: concept
tags: [teams, channel-agent, purview, ediscovery, governance, compliance]
last_modified_at: 2026-07-30
excerpt: "Teams에서 메시지를 지워도 흔적이 남는 두 가지 다른 제약이 있다. 하나는 삭제 후 남는 **tombstone('이 메시지가 삭제되었습니다')** 으로, 이는 네이티브로 제거할 수 없고 채널 자체를 지우는 것이 유일한 방법이다. 다른 하나는 **봇·채널 에이전트가 작성한 메시지**로, Teams가 '내가 쓴 메시지'에만 삭제 옵션을 띄우기 때문에 삭제 "
---

<span class="wiki-type-badge">concept</span>

## Summary

Teams에서 메시지를 지워도 흔적이 남는 두 가지 다른 제약이 있다. 하나는 삭제 후 남는
**tombstone("이 메시지가 삭제되었습니다")** 으로, 이는 네이티브로 제거할 수 없고 채널
자체를 지우는 것이 유일한 방법이다. 다른 하나는 **봇·채널 에이전트가 작성한 메시지**로,
Teams가 "내가 쓴 메시지"에만 삭제 옵션을 띄우기 때문에 삭제 버튼이 아예 나타나지 않는다.
후자는 "삭제 불가"가 아니라 권한·작성자 문제이며 관리자 레벨에서는 지울 수 있다.

## Key Facts

- 채널에서 메시지를 지우면 원문만 사라지고 **시스템 자리표시자(tombstone)** 가 남는다.
  로컬 캐시가 아니라 **대화 기록의 일부**라 캐시 삭제나 앱 재설치로도 사라지지 않는다.
  [출처: sources/012-teams-message-deletion-constraints.md]
- tombstone은 삭제한 본인뿐 아니라 **채널 구성원 전원에게 동일하게** 보인다. 관리자가
  지워도 "관리자가 이 메시지를 제거했습니다"로 문구만 바뀔 뿐 흔적은 남는다.
  [출처: sources/012-teams-message-deletion-constraints.md]
- **채널 자체를 삭제하는 것이 tombstone까지 없애는 유일한 확실한 방법이다.**
  [출처: sources/012-teams-message-deletion-constraints.md]
- 보존정책(Purview Retention)과 eDiscovery purge는 **원문을 영구 소각하는 도구이지
  tombstone 표시를 지우는 도구가 아니다.** 문구만 치환된다.
  [출처: sources/012-teams-message-deletion-constraints.md]
- 채널 에이전트의 답변은 **봇(앱)이 작성자로 게시한 별도의 채널 메시지**다. Teams는
  "내가 작성한 메시지"에만 삭제 옵션을 노출하므로 멤버든 소유자든 삭제가 뜨지 않는다.
  [출처: sources/012-teams-message-deletion-constraints.md]
- **Teams 관리자는 작성자가 누구든(봇 포함) 개별 메시지를 삭제할 수 있다.** 단 스레드
  답글도 한 개씩 지워야 하고 원글+답글 일괄 삭제는 지원하지 않는다.
  [출처: sources/012-teams-message-deletion-constraints.md]

## Details

### tombstone 제거 방법별 정리

| 방법 | 흔적 제거 | 비고 |
|------|:---:|------|
| 개별 tombstone 삭제 | ✕ | 네이티브 기능 없음 (2026 현재) |
| **채널 자체 삭제** | ◎ | 스레드·댓글·tombstone 전부 제거 |
| 보존정책 삭제 | △ | "조직 보존정책이 삭제함"으로 치환. 반영 최대 3일 |
| eDiscovery purge | △ | "관리자가 제거함"으로 치환. SubstrateHolds 이동 후 1~7일 뒤 영구삭제 |

이는 버그가 아니라 **대화 기록 무결성을 위한 의도된 설계**다. 특정 스레드만 정리하고
싶다면 살릴 내용을 새 채널로 재구성한 뒤 기존 채널을 폐기하는 것이 현실적이다. 애초에
흔적을 덜 남기려면 메시징 정책에서 삭제 권한을 조정하거나, 민감한 논의는 채널 대신
정리 부담이 적은 공간에서 한다.
[출처: sources/012-teams-message-deletion-constraints.md]

### 봇/에이전트 메시지 삭제 경로 (확실한 순서)

1. **Teams 관리자로 삭제** — 가장 확실. 작성자 무관하게 개별 삭제 가능.
2. **메시징 정책 `Owners can delete sent messages` 토글** — 이론상 가능하나 **실측
   필요**. 켜도 봇/앱 메시지엔 옵션이 안 뜨거나 자기 메시지만 지워지는 사례가 커뮤니티에
   보고돼 있다.
3. **에이전트를 채널에서 삭제** — "관련 데이터도 함께 삭제"된다고 명시돼 있으나 **이미
   게시된 버블까지 소급 제거되는지는 문서에 없어 실측 대상**이다.
4. **완전 제거 목적이면** Purview eDiscovery/보존 정책으로 조직 차원 삭제.
   [출처: sources/012-teams-message-deletion-constraints.md]

### 채널 에이전트 관련 부가 사실

- 채널 에이전트 기능 자체가 조사 시점에 **public preview** 단계라 동작이 바뀔 수 있다.
- 에이전트가 흡수한 **지식(요약) 제거는 메시지 삭제와 별개**다. 24시간 승인 창 이후에도
  요약 제거가 가능하며, 제거 시점 이후 응답부터 그 정보를 쓰지 않는다.
- 에이전트 **상태 보고서**는 채널 SharePoint의 Channel 폴더에 `.loop` 파일로 저장되고
  작성자가 에이전트 생성자이므로, Loop 파일로 편집/삭제한다.
  [출처: sources/012-teams-message-deletion-constraints.md]

### 판단 원칙 — "안 보인다"와 "불가능하다"를 구분할 것

봇 메시지 삭제 버튼이 없는 것은 기능 부재가 아니라 **작성자 기준 UI 노출 규칙**의 결과다.
문서에 명시가 없다는 이유로 "삭제 불가"라고 단정하면 관리자 경로라는 실제 해법을 놓친다.
반대로 3번(에이전트 삭제 시 소급 제거)처럼 문서에 근거가 없는 항목은 단정하지 말고
실측 대상으로 남겨야 한다.

## Connections

- → [[Copilot Chat 응답 모드와 작업 모델의 2계층 구조]] : 같은 계열의 "공개 문서만으로는
  확정되지 않아 실측이 필요한 M365 프리뷰 기능" 사례.

## Open Questions

- 에이전트를 채널에서 삭제할 때 이미 게시된 답글 버블이 소급 제거되는지 — 문서 근거 없음,
  실측 필요.
- `Owners can delete sent messages` 토글이 봇/앱 메시지에 실제로 적용되는지 — 커뮤니티
  보고가 엇갈려 테넌트별 실측 필요.
- 채널 에이전트가 public preview를 벗어난 뒤 개별 응답 삭제 기능이 추가되는지.
