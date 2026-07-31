---
title: "SharePoint 항목 수준 권한의 일괄 제어와 확장 한계"
wiki_type: concept
tags: [sharepoint, permissions, power-automate, pnp-powershell, governance, scalability]
last_modified_at: 2026-07-30
excerpt: "SharePoint 리스트에서 '여러 항목을 골라 한 번에 권한을 주는' 네이티브 기능은 없다. 권한은 항목마다 상속을 끊어 개별 부여하는 구조라, 다수 항목 제어는 자동화(Power Automate, PnP PowerShell)로만 가능하다. 더 중요한 건 이 방식이 **성능·확장성 리스크가 큰 설계**라는 점이다. 고유 보안 범위는 목록당 5,000개가"
---

<span class="wiki-type-badge">concept</span>

## Summary

SharePoint 리스트에서 "여러 항목을 골라 한 번에 권한을 주는" 네이티브 기능은 없다. 권한은
항목마다 상속을 끊어 개별 부여하는 구조라, 다수 항목 제어는 자동화(Power Automate,
PnP PowerShell)로만 가능하다. 더 중요한 건 이 방식이 **성능·확장성 리스크가 큰 설계**라는
점이다. 고유 보안 범위는 목록당 5,000개가 권장 상한이고 50,000개가 하드 리밋이라,
항목 권한을 잘게 쪼개는 대신 권한 경계를 상위(목록·사이트)로 올리는 편이 지속가능하다.

## Key Facts

- SharePoint 네이티브 UI에는 **여러 항목을 체크해 한 번에 권한을 부여하는 기능이 없다.**
  [출처: sources/011-sharepoint-item-level-permissions.md]
- 목록 고급 설정의 "항목 수준 권한"은 이름과 달리 **임의로 고른 다수가 아니라 "작성자
  본인 것만 vs 전체"** 라는 작성자 기준 통제다.
  [출처: sources/011-sharepoint-item-level-permissions.md]
- 고유 보안 범위(unique security scope) **하드 리밋은 목록당 50,000개, 권장 상한은
  5,000개.** 상속을 끊은 항목 하나가 1 scope로 카운트된다.
  [출처: sources/011-sharepoint-item-level-permissions.md]
- 5,000 초과 시 ACL이 커져 속도가 저하되고 List View Threshold(5,000)와 얽혀 뷰가 깨질 수
  있다. 50,000 초과 시 `"You cannot break inheritance… too many items with unique
  permissions"` 에러로 차단된다.
  [출처: sources/011-sharepoint-item-level-permissions.md]
- **뷰(View) 필터와 대상 그룹(Audience Targeting)은 보안 경계가 아니다.** 화면에서 안 보일
  뿐 URL·검색·API로 접근 가능하다.
  [출처: sources/011-sharepoint-item-level-permissions.md]
- MS는 항목 수준 고유 권한을 "가능한 한 적게 쓰라"고 공식 권고한다.
  [출처: sources/011-sharepoint-item-level-permissions.md]

## Details

### 방법별 비교

| 방법 | 다수 항목 처리 | 성격 | 적합 상황 |
|------|:---:|------|-----------|
| ① 네이티브 UI (Manage access) | ✕ (1건씩) | 항목 선택 → 상속 끊고 부여 | 소량, 예외 몇 건 |
| ② 목록 고급 설정 "항목 수준 권한" | △ (작성자 기준) | "본인 것만/모두 읽기" | 작성자 단위 통제만 |
| ③ Power Automate | ○ | 컬럼값 기준 자동 부여 (노코드) | 실무 1순위 |
| ④ PnP PowerShell | ◎ | 조건/ID 목록 대량 스크립트 | 대량 일괄, 관리자 |
| ⑤ Graph API / CSOM | ◎ | 코드 통합 | 개발 연동 |
| ⑥ 서드파티(ShareGate 등) | ◎ | GUI 일괄 권한 | 툴 도입 조직 |

### 실무 패턴 — 컬럼값 기반 자동 부여

임의로 여러 개를 고르는 것보다 **"이 조건이면 열람 허용"을 컬럼 하나로 정의**하는 편이
유지보수가 쉽다. 조건이 데이터에 있으면 흐름이 멱등해지고, 대상이 바뀌어도 스크립트를
고칠 필요가 없다.

PnP PowerShell은 `Get-PnPListItem`에 CAML 쿼리로 대상을 좁힌 뒤
`Set-PnPListItemPermission -AddRole "Read" -ClearExisting`으로 상속을 끊고 부여한다.
Power Automate는 "SharePoint에 HTTP 요청 보내기"로 항목마다 두 번 호출한다 —
`breakroleinheritance(copyRoleAssignments=false,clearSubscopes=true)` 후
`roleassignments/addroleassignment(principalid=…,roledefid=1073741826)`이며
`1073741826`이 읽기 권한 수준이다.
[출처: sources/011-sharepoint-item-level-permissions.md]

### 설계 관점 권장안

항목 권한을 잘게 쪼개는 대신 **권한 경계 자체를 상위로 올린다.**

- 열람 대상이 명확히 갈리면 목록/라이브러리 또는 사이트를 분리해 그 단위로 권한 부여
- 정말 항목 단위 통제가 필요하면 5,000 미만으로 설계
- 부여 대상은 개인이 아니라 **그룹**으로 — 인원 변동 시 권한을 다시 훑지 않아도 된다
  [출처: sources/011-sharepoint-item-level-permissions.md]

## Connections

- → [[Henry Agentic System]] : 컬럼값 기반 자동 부여는 "조건을 데이터에 두고 실행을
  자동화한다"는 하네스 운영 원칙과 같은 형태다.

## Open Questions

- 5,000 권장 상한을 넘긴 기존 목록을 분할할 때의 안전한 마이그레이션 순서(권한 재설계 →
  항목 이관 → 상속 복구)는 아직 정리된 절차가 없다.
