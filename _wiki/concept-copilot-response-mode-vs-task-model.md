---
title: "Copilot Chat 응답 모드와 작업 모델의 2계층 구조"
wiki_type: concept
tags: [m365-copilot, copilot-chat, agentic, model-routing, governance]
last_modified_at: 2026-07-30
excerpt: "2026년 7월 기준 M365 Copilot Chat의 모델 피커에는 성격이 다른 두 계층이 섞여 있다. 하나는 '얼마나 오래 생각할지'를 고르는 **응답 스타일**(Auto / 빠른 응답 / 심층 분석)이고, 다른 하나는 '여러 단계에 걸쳐 일을 수행할지'를 고르는 **작업 모델**(고급 작업)이다. 이름이 비슷해 같은 축으로 오해하기 쉽지만 축 자체가 "
---

<span class="wiki-type-badge">concept</span>

## Summary

2026년 7월 기준 M365 Copilot Chat의 모델 피커에는 성격이 다른 두 계층이 섞여 있다.
하나는 "얼마나 오래 생각할지"를 고르는 **응답 스타일**(Auto / 빠른 응답 / 심층 분석)이고,
다른 하나는 "여러 단계에 걸쳐 일을 수행할지"를 고르는 **작업 모델**(고급 작업)이다.
이름이 비슷해 같은 축으로 오해하기 쉽지만 축 자체가 다르며, 이 구분을 놓치면 기능 설명과
거버넌스 판단이 모두 어긋난다.

## Key Facts

- 개별 GPT 모델명을 직접 고르던 방식이 **응답 방식(response mode) 선택**으로 재편됐다.
  Auto / Quick Response(빠른 응답) / Think Deeper(심층 분석) 체계다.
  [출처: sources/010-ms-copilot-model-tiers-2026-07.md]
- **고급 작업(Advanced tasks)은 심층 분석과 다른 축이다.** 추론 깊이 조절이 아니라 여러
  단계에 걸친 실제 작업 수행(agentic, long-running, multi-step)을 하는 별도 실행 계층이며,
  MS의 에이전틱 실행 라인(Copilot Tasks / Copilot Cowork)을 Chat 피커에 얹은 형태다.
  [출처: sources/010-ms-copilot-model-tiers-2026-07.md]
- 심층 분석은 더 오래 추론할 뿐 결국 **한 번의 답변**을 돌려주고, 고급 작업은 계획 수립 →
  앱·웹을 넘나드는 실행 → 완료 보고로 이어지는 **분~시간 단위 작업**이다.
  [출처: sources/010-ms-copilot-model-tiers-2026-07.md]
- 고급 작업은 단일 모델이 아니라 멀티모델 스택(Claude Opus 계열 / GPT-5.6 / Auto 라우팅)에
  물린다. [출처: sources/010-ms-copilot-model-tiers-2026-07.md]
- GPT-5.6은 2026-07-09부터 Word·Excel·PowerPoint·Chat·Cowork 5개 표면의 preferred
  model이다. "preferred"는 강제 기본값이 아니라 **배포·라우팅 신호**이며, 새 동의나
  거버넌스 변경을 수반하지 않는다. [출처: sources/010-ms-copilot-model-tiers-2026-07.md]
- 고급 작업은 **동의 게이트(consent)** 를 가진다. 돈을 쓰거나 메일을 보내는 등 의미 있는
  행동 전에 사용자 확인을 요청한다. MS 공식 표현은 "autopilot이 아니라 copilot"이다.
  [출처: sources/010-ms-copilot-model-tiers-2026-07.md]

## Details

### 두 계층의 대비

| | 심층 분석 (Think Deeper) | 고급 작업 (Advanced tasks) |
|---|---|---|
| 성격 | 응답 **깊이** 조절 | **작업 실행** 방식 |
| 결과물 | 더 오래 추론한 한 번의 답 | 여러 단계를 거친 실제 산출물/행동 |
| 동작 | 즉석 대화 | 계획 수립 → 앱·웹 넘나들며 실행 → 완료 후 보고 |
| 실행 위치 | 대화창 안 | 자체 클라우드 컴퓨트 + 통제된 브라우저에서 백그라운드 실행 |
| 소요 | 초 단위 | 분~시간 단위(long-running) |

즉 **심층 분석은 "깊게 대답", 고급 작업은 "일을 여러 단계로 수행"** 이다.

### 관리자 컨트롤이 상위 게이트

응답 모드 피커는 사용자에게 노출되지만, 실제로 어떤 모델이 백엔드에 물릴지는 관리센터
설정이 상위에서 결정한다. 관리센터 > Copilot 설정에서 개별 모델을 켜고 끌 수 있고,
Anthropic(Claude) 계열은 전체 토글이 제공된다(2026-05-05부터 사용자·그룹별 액세스 제어).
[출처: sources/010-ms-copilot-model-tiers-2026-07.md]

2026-07-24부로 GPT-5.6의 "OpenAI-operated provider(OpenAI 직접 API 경로)"가 기본
활성화됐다. 관리자가 사전에 opt-out 하지 않으면 데이터가 Azure가 아니라 OpenAI 인프라를
거치게 되며 FedRAMP High·PCI DSS·HITRUST·SOC1 보장 범위가 달라질 수 있다. 정부·소버린
클라우드는 애초 제외다. 경로는 관리센터 > Copilot > Settings > View all > "AI providers
operating as Microsoft subprocessors"이며 전체 허용 / 특정 그룹만 / 비활성화를 고른다.
[출처: sources/010-ms-copilot-model-tiers-2026-07.md]

### phased 롤아웃 — 테넌트마다 화면이 다르다

조기 액세스 테넌트가 개편을 먼저 받지만 롤아웃이 phased라 테넌트마다 피커 모습이 다르다.
라벨이 아직 안 보이면 초기 단계일 수 있고, 반대로 개별 모델명이 다시 잠깐 보이는 경우도
보고된다. 따라서 데모나 교육 전에는 **해당 테넌트의 실제 피커 상태를 먼저 확인**해야 한다.
[출처: sources/010-ms-copilot-model-tiers-2026-07.md]

### 방법론 교훈 — 공개 문서에 없는 프리뷰는 화면이 우선

이 페이지의 핵심 구분은 처음에 틀리게 정리됐다. 최초 조사에서 "고급 작업 = 심층 분석"으로
매핑했으나, 화면을 직접 보고 있던 사용자의 지적으로 정정됐다. 원인은 명확하다. 공개
릴리스 노트에 해당 한국어 라벨이 아직 잡혀 있지 않고, 조기 액세스 테넌트에 먼저 노출되는
프리뷰 기능이라 **일반 문서만으로는 실체를 확인할 수 없었다.**

→ 공개 문서에 라벨이 없는 프리뷰 기능은 문서보다 **실제 화면 관찰이 우선**한다.
[출처: sources/010-ms-copilot-model-tiers-2026-07.md]

### 조사 시 알려진 소스 제약

- MS Learn 릴리스 노트는 조사 시점에 2026-07-15까지만 반영돼 있었다.
- techcommunity 블로그는 WebFetch 시 본문이 비어 반환되는 알려진 이슈가 있다.
- 2차 블로그마다 모델 버전 표기(5.2/5.4/5.5/5.6)가 시점 차로 엇갈린다.
  [출처: sources/010-ms-copilot-model-tiers-2026-07.md]

## Connections

- → [[Teams 메시지 삭제의 구조적 제약]] : 같은 계열의 "공개 문서만으로는 확정되지 않고
  실측이 필요한 M365 프리뷰 기능" 사례. 채널 에이전트도 public preview 단계였다.
- → [[Henry Agentic System]] : 조기 액세스 기능의 실체 확인이 필요할 때 리서치 에이전트
  단독 조사로는 부족하고 사용자 실측이 개입해야 한다는 하네스 운영 원칙과 연결된다.

## Open Questions

- 고급 작업이 **Copilot Tasks(개인 에이전트)** 계열인지 **Cowork(엔터프라이즈 에이전트)**
  계열인지는 미확정. 피커에서 함께 표기되는 항목(Opus / GPT-5.6 / 에이전트 아이콘)으로
  갈리며, 실측으로만 확정 가능하다.
- 응답 모드 개편과 GPT-5.6이 MS Learn 공식 릴리스 노트에 언제 반영되는지 — 반영되면
  2차 소스 의존을 걷어내고 이 페이지의 근거를 공식 문서로 교체해야 한다.
