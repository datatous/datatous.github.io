---
title: "About · 텍스트 소개"
permalink: /profile/
layout: single
author_profile: false
toc: true
toc_sticky: true
toc_label: "About Henry"
header:
  overlay_image: /assets/images/header-banner.png
  overlay_filter: 0.35
excerpt: "AX 컨설턴트 Henry입니다.<br>AI와 데이터로 일하는 방식을 다시 설계합니다."
---

<div class="view-toggle" markdown="0">
  <span class="view-toggle__label">📄 텍스트 소개</span>
  <a class="view-toggle__btn" href="/about/">🎮 캐릭터 시트로 보기 →</a>
</div>
<style>
.view-toggle{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;
  background:#eff6ff;border:1px solid #dbeafe;border-radius:12px;padding:10px 16px;margin:0 0 14px;
  font-family:'Pretendard',sans-serif;}
.view-toggle__label{font-weight:800;color:#1d4ed8;font-size:.95rem;}
.view-toggle__btn{font-weight:700;color:#fff!important;background:#2563eb;border-radius:99px;
  padding:7px 16px;font-size:.86rem;text-decoration:none!important;transition:background .15s;}
.view-toggle__btn:hover{background:#1d4ed8;}
/* 2026-11-27 구조 개편: 핵심 성과 먼저, 세부는 아래로 */
.page__hero--overlay{padding:1.7em 0;}
@media (min-width:48em){.page__hero--overlay{padding:2em 0;}}
@media (max-width:63.99em){.page__content .sidebar__right{display:none;}}
.pf-now{margin:0;padding:13px 16px 14px;border:1px solid var(--accent-border);border-radius:16px;
  background:linear-gradient(135deg,var(--accent-soft) 0%,#fff 72%);}
.page__content .pf-now + h2{margin-top:1.3em;}
.pf-eyebrow{display:block;font-family:'Sora','Pretendard Variable',Pretendard,sans-serif;font-weight:700;
  font-size:.72rem;letter-spacing:.16em;color:var(--accent);}
.pf-now .pf-role{margin:.25em 0 .2em;font-weight:800;font-size:1.15rem;line-height:1.35;letter-spacing:-.02em;color:var(--ink);}
.pf-now .pf-role a{color:inherit;text-decoration:none;border-bottom:2px solid var(--accent-border);}
.pf-now .pf-role a:hover{border-bottom-color:var(--accent);}
.pf-now p{margin:0;font-size:.92rem;line-height:1.65;color:var(--ink-2);}
.pf-proof{display:grid;gap:8px;margin:.8rem 0 .7rem;}
.pf-row{display:grid;grid-template-columns:1fr auto;grid-template-areas:"num src" "txt txt";gap:2px 12px;
  padding:11px 14px 12px 16px;background:#fff;border:1px solid #dbe4f0;border-left:3px solid var(--accent);border-radius:14px;}
.page__content .pf-num{grid-area:num;margin:0 0 4px;line-height:1.15;color:var(--accent-ink);white-space:nowrap;}
.pf-num b{font-family:'Sora','Pretendard Variable',Pretendard,sans-serif;font-weight:700;font-size:1.6rem;letter-spacing:-.02em;}
@media (min-width:48em){.pf-num b{font-size:1.75rem;}}
.pf-num small{margin-left:3px;font-size:.92rem;font-weight:700;}
.pf-src{grid-area:src;align-self:start;margin-top:4px;padding:2px 10px;border:1px solid #e2e8f0;border-radius:999px;
  background:#f8fafc;color:#475569;font-size:.72rem;font-weight:700;white-space:nowrap;}
.pf-txt{grid-area:txt;}
.pf-txt p{margin:0;}
.pf-what{font-weight:700;font-size:.98rem;line-height:1.5;color:var(--ink);}
.pf-so{margin-top:2px!important;font-size:.9rem;line-height:1.6;color:#475569;}
.page__content .pf-note{margin:0 0 .5rem;font-size:.85rem;color:var(--muted);}
@media (min-width:48em){
  .pf-proof{grid-template-columns:1fr 1fr;gap:10px;}
  .pf-row{padding:13px 16px 14px 18px;align-content:start;}
}
.pf-flow{list-style:none;margin:1rem 0 0;padding:0;}
.pf-flow li{position:relative;margin:0;padding:0 0 18px 24px;}
.pf-flow li::before{content:"";position:absolute;left:3px;top:.42em;width:11px;height:11px;border-radius:50%;
  background:#fff;border:2px solid var(--accent-border);}
.pf-flow li.is-now::before{background:var(--accent);border-color:var(--accent);}
.pf-flow li::after{content:"";position:absolute;left:8px;top:1.5em;bottom:2px;width:1px;background:#dbe4f0;}
.pf-flow li:last-child{padding-bottom:0;}
.pf-flow li:last-child::after{display:none;}
.pf-when{display:block;font-family:'Sora','Pretendard Variable',Pretendard,sans-serif;font-weight:600;
  font-size:.74rem;letter-spacing:.04em;color:var(--muted);}
.pf-org{display:block;font-weight:800;line-height:1.45;color:var(--ink);}
.pf-org a{color:inherit;}
.pf-did{display:block;margin-top:2px;font-size:.9rem;line-height:1.65;color:#475569;}
.page__content details.pf-more{margin:.8rem 0 1.1rem;padding:0 16px;border:1px solid #dbe4f0;border-radius:14px;background:#f8fafc;}
.page__content details.pf-more[open]{background:#fff;padding-bottom:10px;}
.pf-more summary{cursor:pointer;padding:11px 0;font-weight:700;font-size:.93rem;color:var(--ink);}
.pf-more summary small{margin-left:.4em;font-weight:600;color:var(--muted);}
.pf-more summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:6px;}
.pf-more ul{margin:.2rem 0 .4rem;padding-left:1.2em;}
.pf-more li{margin:.25em 0;font-size:.93rem;line-height:1.7;}
.pf-more table{display:table;width:100%;margin:.3rem 0 .6rem;font-size:.86rem;}
.pf-more th{width:7.5em;vertical-align:top;color:var(--ink);}
</style>

<div class="pf-now" markdown="0">
  <span class="pf-eyebrow">NOW · 2026.02~</span>
  <p class="pf-role"><a href="https://www.munilabs.co.kr/">무늬랩스</a> AX 컨설턴트</p>
  <p>대기업의 M365 Copilot·AX 도입을 돕는다. 그 전에는 공공기관(KCA)에서 데이터와 자동화를, 한국능률협회(KMA)에서 AX 교육을 맡았다.</p>
</div>

## 핵심 성과

<div class="pf-proof" markdown="0">
  <div class="pf-row">
    <p class="pf-num"><b>13,019</b><small>명</small></p>
    <div class="pf-txt"><p class="pf-what">KT AX 디그리 2.0 수강생</p><p class="pf-so">AI 전환 교육을 운영하며 수료 6,124명, 전문가 심층 피드백 993건을 지원했다.</p></div>
    <span class="pf-src">KMA · 2025</span>
  </div>
  <div class="pf-row">
    <p class="pf-num"><b>9,392</b><small>시간 / 년</small></p>
    <div class="pf-txt"><p class="pf-what">RPA 9건으로 줄인 행정업무 시간</p><p class="pf-so">절감한 인력 4명은 신규 사업으로 옮겨 갔다.</p></div>
    <span class="pf-src">KCA · 2023–24</span>
  </div>
  <div class="pf-row">
    <p class="pf-num"><b>3만+</b><small>다운로드</small></p>
    <div class="pf-txt"><p class="pf-what">ChatGPT 업무활용 가이드북 2.0</p><p class="pf-so">집필·개정을 총괄했고 교육영상 9건도 따로 만들었다.</p></div>
    <span class="pf-src">KCA · 2024</span>
  </div>
  <div class="pf-row">
    <p class="pf-num"><b>2</b><small>년 연속 '우수'</small></p>
    <div class="pf-txt"><p class="pf-what">공공데이터·데이터기반행정 평가, 기관 최초</p><p class="pf-so">품질관리 만점을 받았고 2024년 과기정통부 장관 표창으로 이어졌다.</p></div>
    <span class="pf-src">KCA · 2023–24</span>
  </div>
</div>
<p class="pf-note" markdown="0">성과 기록 28건 가운데 넷만 먼저 꺼냈다. 나머지는 아래 대표 프로젝트와 <a href="/about/">캐릭터 시트</a>에 있다.</p>

## 경력 흐름

<ol class="pf-flow" markdown="0">
  <li class="is-now"><span class="pf-when">2026.02 ~</span><span class="pf-org"><a href="https://www.munilabs.co.kr/">무늬랩스 (MUNI LABS)</a> · AX 컨설턴트</span><span class="pf-did">대기업 M365 Copilot·AX 도입 컨설팅. 활용 미션 설계, 현업 밀착 가이드(인터뷰·FGI·세션), 성과 데이터 분석과 최종 보고, Power Platform·Copilot Studio 기술 컨설팅. 틈틈이 에이전틱 시스템을 직접 만들어 운용</span></li>
  <li class="is-now"><span class="pf-when">2025.03 ~</span><span class="pf-org">성균관대학교 정보통신대학원 · 빅데이터학과 석사</span><span class="pf-did">2027년 8월 졸업을 목표로 일과 연구를 병행 중</span></li>
  <li><span class="pf-when">2025.03 ~ 2025.12</span><span class="pf-org">한국능률협회 (KMA)</span><span class="pf-did">KT AX 디그리 2.0 운영, Power Platform 현장 컨설팅, AX in:site 성과공유 플랫폼 구축 (KT 전사 오픈)</span></li>
  <li><span class="pf-when">2022.04 ~ 2025.03</span><span class="pf-org">한국방송통신전파진흥원 (KCA)</span><span class="pf-did">데이터 품질·개방·정책연구, RPA 플랫폼, 차세대 행정시스템 클라우드 전환 (26억 사업)</span></li>
  <li><span class="pf-when">~ 2022</span><span class="pf-org">공공 교육 플랫폼 운영 1년</span><span class="pf-did">충남대학교 경영학·컴퓨터공학 복수전공 / 캐나다 토론토 1년</span></li>
</ol>

## 대표 프로젝트

**KT AX 디그리 2.0 & AX in:site**: 13,019명 규모 AI 전환 교육의 기술지원과 우수사례 확산 플랫폼(SharePoint, 콘텐츠 126건)을 함께 운영했다. 교육과 시스템, 양쪽에서 AX가 정착되는 구조를 만들었다. (Power Platform · SharePoint · Power BI)

**식수인원 예측모델**: 내외부 18개 요인으로 구내식당 식수를 예측(R² 0.85)해 잔반을 줄이고, 절감분을 지역 소외계층 무료급식 캠페인으로 연결했다. 분석이 사회적 가치까지 이어진 가장 아끼는 프로젝트. (Python · scikit-learn)

**과기정통부 데이터 활용 정책연구 (2년)**: 국가R&D 과제 두 건에 참여연구원으로 함께했다. 약 20개 기관의 데이터 분석과제를 컨설팅하고 정책 보고서 2건을 발간했다. 2024년 과학기술정보통신부 장관 표창으로 이어졌다. 과제명은 아래 [자격·연구·도구](#자격연구도구)에 있다.

**RPA 플랫폼 & 차세대 시스템 클라우드 전환**: 반복 행정업무 자동화(연 9,392시간 절감)와 26억 규모 클라우드 전환 사업을 함께 수행하며, 절감된 시간이 신규 사업 인력 4명으로 전환되는 것을 확인했다.

**Henry's Agentic System**: Claude Code 기반 멀티 에이전트 하네스. 글쓰기·MS 업데이트 추적·지식 위키·블로그 발행 등 도메인별 워커가 협업하는 개인 자동화 인프라이고, 이 블로그가 그 쇼케이스다. 2026년 9월에는 반년 동안 불어난 구조를 실측으로 진단해 워커 14→9개, 세션 고정 로딩 −31%로 줄이고, 다시 불어나지 않게 스스로 재는 점검기를 붙였다. → [케이스 스터디](/posts/harness-v12-slimming/) (Claude Code · Python · Mermaid)

## 무엇을 하는 사람인가

### 1. AX 컨설팅 & 변화관리

조직이 AI를 '도입'하는 것과 '체화'하는 것은 다르다. 교육 설계부터 현장 코칭, 변화관리까지 맡아서 기술이 실제 업무 방식의 변화로 이어지는 마지막 구간을 책임진다.

<details class="pf-more" markdown="0"><summary>근거 보기 <small>4건</small></summary>
<ul>
<li>DX/AX 변화관리 및 조직문화 컨설팅</li>
<li>KT AX 디그리 2.0 운영: <strong>수강생 13,019명, 수료 6,124명</strong> 규모의 AI 전환 교육</li>
<li>ChatGPT 업무활용 가이드북 집필·개정: <strong>다운로드 3만+</strong></li>
<li>MS Power Platform 기술 컨설팅 (Power Automate, Copilot Studio, Power Apps)</li>
</ul>
</details>

### 2. 데이터 분석 & BI

공공기관에서 데이터의 **제공자**(품질관리·개방·인프라)와 **활용자**(분석·정책연구) 양쪽을 모두 경험했다. 분석 자체보다, **분석이 의사결정으로 이어지는 구조**를 만드는 데 관심이 많다.

<details class="pf-more" markdown="0"><summary>근거 보기 <small>5건</small></summary>
<ul>
<li>식수인원 예측모델 (Python 앙상블, R² 0.85): 잔반 절감분을 사회공헌 캠페인으로 연결</li>
<li>무선 네트워크 VOC 분석 → Power BI 품질 대시보드 구축</li>
<li>과기정통부 데이터 활용 정책연구 2년(국가R&amp;D 과제 2건, 참여연구원): 약 20개 기관 분석과제 컨설팅, <strong>과기정통부 장관 표창 (2024.12)</strong></li>
<li>공공데이터·데이터기반행정 평가 <strong>기관 최초 2년 연속 '우수' 등급</strong> 달성 기여</li>
<li>Kaggle Playground: 대출상환 예측 <strong>Top 36%</strong> (AUC 0.924)</li>
</ul>
</details>

### 3. 에이전틱 시스템 & 자동화

Claude Code 위에 나만의 멀티 에이전트 시스템을 운영한다. 반복 작업을 맡기되, 목적과 공개할 결과의 판단은 내 몫으로 둔다. 그리고 늘리는 만큼 **줄이는 것**도 설계한다.

<details class="pf-more" markdown="0"><summary>근거 보기 <small>5건</small></summary>
<ul>
<li>RPA 플랫폼 구축·고도화: <strong>연간 9,392시간 절감</strong> (KCA)</li>
<li>Claude Code 멀티 에이전트 하네스 설계·운용. 라우팅은 <code>CLAUDE.md</code> 표 하나</li>
<li>실측 기반 경량화(v12): 워커 14→9, 세션 고정 로딩 <strong>−31%</strong>, 구조를 스스로 재는 점검기(<code>--check</code>)와 자동 생성 배선도 → <a href="/posts/harness-v12-slimming/">케이스 스터디</a></li>
<li>LLM Wiki 기반 지식 축적 파이프라인 (<a href="/wiki/">Wiki</a>에서 실시간 공개 중)</li>
<li>이 블로그의 발행 파이프라인도 그 산출물이다 → <a href="/categories/#자동화연대기">자동화 연대기</a></li>
</ul>
</details>

## 강점 셋

**1. 문제를 먼저 정의한다.** 약 20개 기관을 컨설팅하며 배웠다. 분석보다 "무엇을 풀 것인가"가 먼저다. 예산 없이 시나리오 분석만으로 시스템 방향을 잡아준 경험이 여럿 있다.

**2. 양쪽 관점을 안다.** 데이터를 만들고 개방하는 쪽과 가져다 분석하는 쪽, 개발자와 현업 사이. 늘 중간에서 통역해온 덕에 "왜 안 되는지"를 양쪽 언어로 설명할 수 있다.

**3. 좋은 건 먼저 써본다.** 취미가 '좋은 것을 찾아 먼저 써보는 것'이다. 그 습관이 가이드북 집필, AI 쇼츠 제작, 에이전틱 하네스 운영으로 이어졌다.

## 자격·연구·도구

<details class="pf-more" markdown="0"><summary>수상·자격 <small>수상 1 · 자격 6</small></summary>
<ul>
<li><strong>과학기술정보통신부 장관 표창</strong> (2024.12, 공공데이터 활성화 유공)</li>
<li>Google Analytics Certification (2026.01)</li>
<li>NAVER Cloud Certified Associate (2025.12)</li>
<li>ADsP (2023.03)</li>
<li>사회조사분석사 2급 (2021.06)</li>
<li>SQLD (2020.01)</li>
<li>컴퓨터활용능력 1급 (2019.11)</li>
</ul>
</details>
<details class="pf-more" markdown="0"><summary>국가R&amp;D 연구과제 <small>2건 · 참여연구원</small></summary>
<ul>
<li>2024.05~2024.11 · 「데이터 분석·활용 컨설팅을 통한 업무 개선방안 연구」 (과기정통부, IITP 방송통신정책연구 R&amp;D)</li>
<li>2023.05~2023.12 · 「데이터기반 행정 문화조성·확산에 관한 방안 연구」 (과기정통부)</li>
</ul>
</details>
<details class="pf-more" markdown="0"><summary>도구와 기술 <small>5개 영역</small></summary>
<table>
<tbody>
<tr><th>Languages</th><td>Python, SQL</td></tr>
<tr><th>BI / Analytics</th><td>Power BI, Tableau, GA4</td></tr>
<tr><th>MS 365</th><td>Power Automate, Copilot Studio, Power Apps, SharePoint, Teams</td></tr>
<tr><th>AI / Architecture</th><td>에이전틱 시스템 설계, Prompt Engineering, RAG, LLM 워크플로우</td></tr>
<tr><th>Dev Tools</th><td>Claude Code, VS Code, Git, GCP</td></tr>
</tbody>
</table>
</details>

> 스킬별 숙련도가 궁금하다면 [캐릭터 시트](/about/)에서 볼 수 있어요. 성과 기록 28건으로 계산한 데이터 기반 스탯이에요.

## 이 블로그는

AX 컨설턴트로 일하면서 클라이언트한테는 "이거 자동화하면 좋아요"라고 말하면서, 정작 내 반복 업무는 손으로 하고 있다는 걸 깨달았다.

직접 만들어 본 자동화 기록에서 시작했다. 지금은 맡길 수 있는 일이 늘어날수록 내가 끝까지 해야 할 일도 함께 묻는다. 시작한 이유는 [첫 글](/posts/what-we-keep/)에 적었다.

이 블로그에서는 **‘AI에게 무엇을 넘기지 않을까’**를 묻는다. 트렌드·논문·책은 [서가](/keep/)에 모으고, 자동화 연대기는 직접 맡겨 본 [현장 기록](/#field)으로 남겨 뒀다. 공부하고 만든 개념은 [Wiki](/wiki/)에 쌓는다.

## Contact

- **GitHub**: [@datatous](https://github.com/datatous)
- **Email**: [datatous25@gmail.com](mailto:datatous25@gmail.com)
- **LinkedIn**: [henry-oh-data](https://www.linkedin.com/in/henry-oh-data)
- **Kaggle**: [@seeingoh](https://www.kaggle.com/seeingoh)
- **Naver Blog**: [blog.naver.com/oh_seeing](https://blog.naver.com/oh_seeing)
- **Instagram**: [@henryo.o](https://www.instagram.com/henryo.o/)

> 자동화 아이디어, 협업, 강의 문의 모두 환영합니다. 🌿
