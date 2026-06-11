---
title: "나는 게을러서 자동화한다 : 1주에 하나씩, 일상을 바꾼 기록"
date: 2026-05-04
categories:
  - 자동화연대기
tags:
  - 자동화
  - AI활용
  - AX컨설턴트
  - ClaudeCode
  - 인공지능
header:
  teaser: /assets/images/posts/ep00-cover.png
  overlay_image: /assets/images/posts/ep00-cover.png
  overlay_filter: 0.5
excerpt: "AX 컨설턴트인데 정작 내 반복 업무는 손으로 하고 있었다. 그래서 직접 만들어보기로 했다."
---

## 📱 카드뉴스로 먼저 보기

<div class="cardnews-carousel" markdown="0"><style>.cardnews-carousel{margin:1.4em 0 1.8em;}.cn-track{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding:4px 4px 14px;scroll-padding:4px;}.cn-track::-webkit-scrollbar{height:8px;}.cn-track::-webkit-scrollbar-track{background:transparent;}.cn-track::-webkit-scrollbar-thumb{background:#c8c8c8;border-radius:4px;}.cn-track img{flex:0 0 auto;width:80%;max-width:340px;height:auto;scroll-snap-align:center;border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,.18);}.cn-hint{font-size:.88em;color:#999;text-align:center;margin:.2em 0 0;letter-spacing:.02em;}@media (min-width:768px){.cn-track img{width:300px;}}</style><div class="cn-track"><img src="/assets/images/posts/ep00/01_cover.png" alt="EP.00 표지 — 나는 게을러서 자동화한다"><img src="/assets/images/posts/ep00/02_why.png" alt="매일 AI 얘기를 하는데 내 손은 바빴다"><img src="/assets/images/posts/ep00/03_commute.png" alt="하루 3시간이 사라지고 있었다"><img src="/assets/images/posts/ep00/04_subway-dev.png" alt="지하철을 개발실로 만들었다"><img src="/assets/images/posts/ep00/05_build-first.png" alt="만들고 싶은 게 먼저다"><img src="/assets/images/posts/ep00/06_lineup.png" alt="앞으로 만들 것들 — 8편 라인업"><img src="/assets/images/posts/ep00/07_principle.png" alt="직접 써보고 이해한 것만 쓴다"><img src="/assets/images/posts/ep00/08_closing.png" alt="자동화 연대기 — 팔로우하고 같이 만들어봐요"></div><p class="cn-hint">← 좌우로 넘겨보세요 →</p></div>

아래는 같은 이야기를 글로 풀어쓴 버전이다.

---

## AI 얘기를 하면서 정작 내 손은 바쁘더라고요 🤔

나는 AX 컨설턴트로 일하고 있다. 기업에 AI 전환(AX)을 컨설팅하고, AI를 어떻게 쓸지 가르치는 일을 한다. 그런데 어느 날 이런 생각이 딱 들었다.

> '나는 매일 AI 얘기를 하는데, 정작 내가 직접 만든 건 얼마나 되지?'

클라이언트한테 "이걸 자동화하면 좋아요"라고 말하면서 정작 내 반복 업무는 여전히 손으로 하고 있었다. 앞뒤가 안 맞았다. 좀 찔렸다. 그래서 직접 만들어보면서 제대로 이해해보기로 했다.

---

## 출퇴근 3시간이 시작점이었어요 🚇

나는 수원에 살고 잠실로 출근한다. 편도 1시간 30분, **하루 왕복 3시간**이 지하철에서 사라진다. 처음엔 그냥 폰 보다가 내렸는데, 어느 날 계산해봤더니 한 달에 60시간이 그냥 증발하고 있었다.

> '이 시간, 그냥 보내기엔 너무 아깝다.'

그래서 지하철에서도 개발할 수 있는 환경을 먼저 세팅했다. Happy 앱에 Claude Code랑 Git 레포를 연결해서 폰으로도 코드 짜고 커밋할 수 있게 만든 거다. 이게 이 모든 것의 출발이었다. (지금은 Claude의 /remote control 커멘드로 바꿔서 쓰고 있다. 이 내용은 추후 정리해서 올려보겠다.)

---

## 내가 배우는 방식 — 만들고 싶은 게 먼저예요 📐

이론 공부하고 실습하는 방식, 나한테 안 맞더라. **만들고 싶은 걸 먼저 정하고, 필요한 기술을 그때 찾아서 배우는 방식**이 훨씬 빠르게 몸에 익는다.

"RAG가 뭔지 공부해야지"가 아니라 "논문 도우미 만들 건데, 어떻게 하지? — 아 이게 RAG구나" 이 순서다. 귀찮음이 학습 동기가 된다. 지금까지 이렇게 배운 게 제일 오래 남더라. 😄

---

## 앞으로 이런 걸 만들어볼 거예요 🗓️

1주에 하나씩, 총 8편을 생각하고 있다. (아래 내용은 변경될 수 있다)

| 편 | 주제 |
|---|---|
| 1편 | 출퇴근 3시간을 개발 시간으로 — Happy + Claude Code + Git 세팅 |
| 2편 | AI가 매주 교회 주보를 올려준다 — 제미나이 Gems + 클로드 에이전틱 자동화 |
| 3편 | 내 블로그를 AI가 대신 써준다 — 깃블로그·네이버 멀티채널 자동 발행 |
| 4편 | 결혼 준비를 함께 뛰는 AI 동행자, '웨딩메이트' — 예산·할 일·참석자 자동화 |
| 5편 | 인스타 카드뉴스를 AI가 찍어낸다 — 카드뉴스 자동 제작 |
| 6편 | 나의 논문 도우미 — RAG로 연구 자료 학습시키기 |
| 7편 | AI에게 스토리를 맡겼더니 — 시나리오 분석 자동화 |
| 8편 | 회고 — 뭐가 달라졌나 |

이미 만들어놓은 것도 있고, 앞으로 만들 것도 있다. **공통점은 하나 — 직접 써보고 이해한 것만 쓴다.**

---

## 이런 분이랑 같이 가고 싶어요 🙌

"AI 써보고 싶은데 어디서부터 시작하지?" "만들고 싶은 건 있는데 코딩 잘 몰라도 되나?" 나도 이 고민에서 시작했다. 코딩 실력보다 **"이거 자동화되면 좋겠다"는 생각** 하나가 더 중요하다.

마치 요리를 배울 때 레시피를 먼저 외우는 것보다 먹고 싶은 게 먼저인 것처럼. 그 배고픔이 원동력이다. 같이 만들어가면서 답 찾아봐요. 😊

---

**나는 게을러서 자동화한다.** 🚀
