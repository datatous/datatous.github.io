---
title: "About"
permalink: /about/
layout: single
author_profile: false
classes: wide
---

<div class="view-toggle" markdown="0">
  <span class="view-toggle__label">🎮 캐릭터 시트</span>
  <a class="view-toggle__btn" href="/profile/">📄 텍스트 소개로 보기 →</a>
</div>

<div class="rpg" markdown="0">
<style>
.view-toggle{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;
  background:#eff6ff;border:1px solid #dbeafe;border-radius:12px;padding:10px 16px;margin:0 0 18px;
  font-family:'Pretendard',sans-serif;}
.view-toggle__label{font-weight:800;color:#1d4ed8;font-size:.95rem;}
.view-toggle__btn{font-weight:700;color:#fff!important;background:#2563eb;border-radius:99px;
  padding:7px 16px;font-size:.86rem;text-decoration:none!important;transition:background .15s;}
.view-toggle__btn:hover{background:#1d4ed8;}
.rpg{--ink:#0f172a;--blue:#2563eb;--sky:#60a5fa;--soft:#eff6ff;--line:#e5e7eb;--muted:#64748b;
  font-family:'Pretendard',sans-serif;}
.rpg *{box-sizing:border-box;}
.rpg .pixel-note{text-align:center;color:var(--muted);font-size:.85rem;margin:.2em 0 1.6em;}

/* ===== hero ===== */
.rpg-hero{background:radial-gradient(120% 160% at 20% 0%,#142446 0%,#0b1220 60%);
  border-radius:20px;padding:38px 28px 30px;color:#fff;position:relative;overflow:hidden;}
.rpg-hero::before{content:"";position:absolute;inset:0;background-image:
  linear-gradient(rgba(96,165,250,.08) 1px,transparent 1px),
  linear-gradient(90deg,rgba(96,165,250,.08) 1px,transparent 1px);background-size:34px 34px;}
.rpg-hero-in{position:relative;display:flex;gap:34px;align-items:center;flex-wrap:wrap;justify-content:center;}
.avatar-henry{width:180px;height:180px;flex:none;
  filter:drop-shadow(0 12px 28px rgba(37,99,235,.4));animation:bob 3s ease-in-out infinite;}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
.avatar-henry .orb{animation:orbpulse 2.4s ease-in-out infinite;transform-origin:center;}
.avatar-henry .orb:nth-child(2){animation-delay:.5s;}
.avatar-henry .orb:nth-child(3){animation-delay:1.1s;}
@keyframes orbpulse{0%,100%{opacity:.5}50%{opacity:1}}
.rpg-id .kicker{font-size:.78rem;letter-spacing:.18em;color:#93c5fd;font-weight:700;}
.rpg-id h2{margin:.15em 0 .1em;font-size:2rem;font-weight:800;letter-spacing:-.02em;color:#fff;border:none;}
.rpg-id .cls{color:#cbd5e1;font-size:1rem;}
.rpg-id .cls b{color:#60a5fa;}
.rpg-badges{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap;}
.rpg-badges span{background:rgba(96,165,250,.14);border:1px solid rgba(96,165,250,.35);
  color:#bfdbfe;font-size:.78rem;font-weight:700;padding:5px 12px;border-radius:999px;}
.rpg-lv{margin-top:14px;font-size:.85rem;color:#94a3b8;}
.rpg-lv b{color:#fff;font-size:1.05rem;}
.xpbar{width:240px;height:10px;background:rgba(255,255,255,.12);border-radius:99px;margin-top:6px;overflow:hidden;}
.xpbar i{display:block;height:100%;width:64%;border-radius:99px;
  background:linear-gradient(90deg,#2563eb,#60a5fa);animation:xpglow 2.2s ease-in-out infinite;}
@keyframes xpglow{0%,100%{opacity:.85}50%{opacity:1}}

/* ===== sections ===== */
.rpg h3.sec{display:flex;align-items:center;gap:.5em;font-weight:800;letter-spacing:-.02em;
  margin:2.2em 0 .8em;border:none;font-size:1.25rem;color:var(--ink);}
.rpg h3.sec::after{content:"";flex:1;height:2px;border-radius:2px;
  background:linear-gradient(90deg,var(--blue),transparent);}

/* stats */
.stat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:14px 26px;}
.stat{padding:4px 0;}
.stat .row{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:5px;}
.stat .nm{font-weight:700;font-size:.95rem;color:var(--ink);}
.stat .nm small{color:var(--muted);font-weight:500;margin-left:.45em;}
.stat .lv{font-weight:800;color:var(--blue);font-size:.92rem;}
.stat .bar{height:12px;background:#eef2f7;border-radius:99px;overflow:hidden;}
.stat .bar i{display:block;height:100%;width:0;border-radius:99px;
  background:linear-gradient(90deg,#2563eb,#60a5fa);transition:width 1.1s cubic-bezier(.22,1,.36,1);}
.stat .src{font-size:.74rem;color:var(--muted);margin-top:4px;}
.stat.up .lv::after{content:" ▲";color:#10b981;font-size:.8em;}

/* class tree */
.tree{display:flex;gap:0;flex-wrap:wrap;align-items:stretch;}
.tree .node{flex:1;min-width:150px;background:#fff;border:1.5px solid var(--line);border-radius:14px;
  padding:14px 14px 12px;position:relative;margin-right:26px;}
.tree .node:last-child{margin-right:0;border-color:var(--blue);
  box-shadow:0 10px 26px rgba(37,99,235,.14);}
.tree .node:not(:last-child)::after{content:"▶";position:absolute;right:-21px;top:50%;
  transform:translateY(-50%);color:#cbd5e1;font-size:.8rem;}
.tree .yr{font-size:.72rem;color:var(--muted);font-weight:700;letter-spacing:.04em;}
.tree .jb{font-weight:800;color:var(--ink);margin:.15em 0 .1em;font-size:.95rem;}
.tree .ds{font-size:.78rem;color:var(--muted);line-height:1.5;}
.tree .node:last-child .jb{color:var(--blue);}

/* equipment */
.equip{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;}
.eq{display:flex;gap:12px;align-items:center;background:#fff;border:1.5px solid var(--line);
  border-radius:14px;padding:12px 14px;}
.eq .ic{width:42px;height:42px;border-radius:10px;display:flex;align-items:center;justify-content:center;
  font-size:1.25rem;flex:none;}
.eq .nm{font-weight:700;font-size:.92rem;color:var(--ink);}
.eq .gr{font-size:.72rem;font-weight:800;letter-spacing:.06em;}
.eq .ds{font-size:.78rem;color:var(--muted);}
.eq.legend{border-color:#f59e0b;}.eq.legend .ic{background:#fef3c7;}.eq.legend .gr{color:#d97706;}
.eq.epic{border-color:#a855f7;}.eq.epic .ic{background:#f3e8ff;}.eq.epic .gr{color:#9333ea;}
.eq.rare{border-color:var(--sky);}.eq.rare .ic{background:var(--soft);}.eq.rare .gr{color:var(--blue);}

/* trophies */
.trophy{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:12px;}
.tp{background:#fff;border:1.5px solid var(--line);border-radius:14px;padding:14px;text-align:center;
  transition:transform .2s,box-shadow .2s;}
.tp:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(15,23,42,.1);}
.tp .em{font-size:1.7rem;}
.tp .tt{font-weight:800;font-size:.86rem;color:var(--ink);margin:.35em 0 .15em;line-height:1.4;}
.tp .ds{font-size:.74rem;color:var(--muted);line-height:1.45;}

/* quests */
.quest{display:flex;flex-direction:column;gap:10px;}
.q{display:flex;gap:13px;align-items:flex-start;background:#fff;border:1.5px solid var(--line);
  border-radius:14px;padding:13px 16px;}
.q .tag{flex:none;font-size:.7rem;font-weight:800;letter-spacing:.05em;padding:4px 10px;
  border-radius:999px;margin-top:2px;}
.q.main .tag{background:#fef3c7;color:#b45309;}
.q.weekly .tag{background:var(--soft);color:var(--blue);}
.q.side .tag{background:#f1f5f9;color:#475569;}
.q .qt{font-weight:700;font-size:.93rem;color:var(--ink);}
.q .qd{font-size:.8rem;color:var(--muted);margin-top:2px;line-height:1.5;}

.rpg-cta{margin-top:2.4em;text-align:center;background:var(--soft);border-radius:16px;padding:22px;}
.rpg-cta a{font-weight:700;}
@media(max-width:640px){.tree{flex-direction:column;}
  .tree .node{margin-right:0;margin-bottom:22px;}
  .tree .node:not(:last-child)::after{content:"▼";right:50%;top:auto;bottom:-19px;transform:translateX(50%);}}
</style>

<!-- ============ HERO ============ -->
<div class="rpg-hero"><div class="rpg-hero-in">
  <svg class="avatar-henry" viewBox="0 0 200 200" role="img" aria-label="Henry 일러스트 아바타">
    <defs>
      <linearGradient id="av-ring" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#60a5fa"/><stop offset="1" stop-color="#2563eb"/>
      </linearGradient>
      <linearGradient id="av-hood" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#e4eefb"/><stop offset="1" stop-color="#c2d6ef"/>
      </linearGradient>
      <clipPath id="av-clip"><rect x="10" y="10" width="180" height="180" rx="48"/></clipPath>
    </defs>
    <rect x="10" y="10" width="180" height="180" rx="48" fill="#0f1d3d"/>
    <rect x="10" y="10" width="180" height="180" rx="48" fill="none" stroke="url(#av-ring)" stroke-width="3"/>
    <g clip-path="url(#av-clip)">
      <!-- shoulders : crisp light-blue collared shirt -->
      <path d="M38 200 C38 156 62 140 100 140 C138 140 162 156 162 200 Z" fill="url(#av-hood)"/>
      <path d="M70 146 L100 176 L130 146" fill="#ffffff" opacity=".5"/>
      <!-- collar -->
      <path d="M86 140 L100 162 L84 152 Z" fill="#fff"/><path d="M114 140 L100 162 L116 152 Z" fill="#fff"/>
      <path d="M86 140 L100 162 L84 152 Z" fill="none" stroke="#aabfdd" stroke-width="1.4"/>
      <path d="M114 140 L100 162 L116 152 Z" fill="none" stroke="#aabfdd" stroke-width="1.4"/>
      <line x1="100" y1="160" x2="100" y2="200" stroke="#aabfdd" stroke-width="1.6"/>
      <circle cx="100" cy="178" r="1.6" fill="#9fb6d8"/>
      <!-- neck -->
      <path d="M89 116 h22 v13 c0 9 -22 9 -22 0 z" fill="#edbf94"/>
      <path d="M89 124 c6 6 16 6 22 0 v5 c0 9 -22 9 -22 0 z" fill="#000" opacity=".05"/>
      <!-- head : oval with defined jaw -->
      <path d="M68 84 C68 105 79 121 100 122 C121 121 132 105 132 84 C132 59 118 49 100 49 C82 49 68 59 68 84 Z" fill="#f7d3aa"/>
      <!-- jaw/cheek soft shading -->
      <path d="M70 90 C73 106 84 118 100 120 C95 118 86 108 82 94 Z" fill="#e7b483" opacity=".35"/>
      <!-- ears -->
      <circle cx="68" cy="90" r="6" fill="#edbf94"/><circle cx="132" cy="90" r="6" fill="#edbf94"/>
      <!-- hair : clean dandy cut, side-swept quiff -->
      <path d="M64 90 C57 73 60 49 84 43 C95 40 109 40 119 45 C137 53 141 75 135 90
               C133 79 129 74 124 73 C126 66 122 60 115 59
               C104 52 86 53 78 60 C71 66 67 76 68 86 C66 87 65 88 64 90 Z" fill="#211a13"/>
      <!-- swept fringe -->
      <path d="M68 84 C70 64 88 56 108 60 C119 62 124 68 124 73
               C113 64 95 63 82 70 C74 74 70 79 68 84 Z" fill="#2b2118"/>
      <!-- hair strand highlights -->
      <path d="M92 49 C84 56 78 64 76 74" stroke="#3a2c1f" stroke-width="2" fill="none" stroke-linecap="round" opacity=".6"/>
      <path d="M108 50 C116 56 121 63 123 71" stroke="#3a2c1f" stroke-width="2" fill="none" stroke-linecap="round" opacity=".5"/>
      <!-- eyes : almond, gentle -->
      <path d="M77 87 Q85 82 93 87" fill="none" stroke="#241c15" stroke-width="2" stroke-linecap="round"/>
      <path d="M107 87 Q115 82 123 87" fill="none" stroke="#241c15" stroke-width="2" stroke-linecap="round"/>
      <ellipse cx="85" cy="89.5" rx="3.4" ry="4" fill="#2a211a"/>
      <ellipse cx="115" cy="89.5" rx="3.4" ry="4" fill="#2a211a"/>
      <circle cx="86.2" cy="88.2" r="1.1" fill="#fff" opacity=".85"/>
      <circle cx="116.2" cy="88.2" r="1.1" fill="#fff" opacity=".85"/>
      <!-- brows : clean, subtle -->
      <path d="M77 80 Q85 77 93 79.5" stroke="#211a13" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      <path d="M107 79.5 Q115 77 123 80" stroke="#211a13" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      <!-- nose -->
      <path d="M100 91 L97 101 Q100 103 103 101" stroke="#dba87a" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- gentle smile -->
      <path d="M91 108 Q100 114 109 108" stroke="#bf7150" stroke-width="2.6" fill="none" stroke-linecap="round"/>
      <!-- cheek blush -->
      <ellipse cx="80" cy="101" rx="4.2" ry="2.6" fill="#f1a085" opacity=".35"/>
      <ellipse cx="120" cy="101" rx="4.2" ry="2.6" fill="#f1a085" opacity=".35"/>
    </g>
    <!-- brand data nodes (datatous motif) -->
    <g class="orb"><circle cx="172" cy="44" r="7" fill="#2563eb"/><circle cx="172" cy="44" r="12" fill="none" stroke="#2563eb" stroke-width="2" opacity=".4"/></g>
    <g class="orb"><circle cx="30" cy="58" r="5" fill="#60a5fa"/></g>
    <g class="orb"><circle cx="44" cy="172" r="4.5" fill="#93c5fd"/></g>
    <polyline points="30,58 44,44 64,50" fill="none" stroke="#60a5fa" stroke-width="2" opacity=".35" stroke-linecap="round"/>
  </svg>
  <div class="rpg-id">
    <div class="kicker">PLAYER PROFILE</div>
    <h2>Henry</h2>
    <div class="cls">Class. <b>AX Consultant</b> · 종족. 게으른 자동화인(2lazysodoit)</div>
    <div class="cls" style="font-size:.86rem;margin-top:6px;color:#94a3b8;">공공 데이터 3년 → AX 교육 13,019명 → 에이전틱 시스템 운영 — 데이터 분석과 자동화로 일하는 방식을 바꿔왔습니다.</div>
    <div class="rpg-badges"><span>📊 Data</span><span>🤖 AI·Agentic</span><span>⚡ Automation</span><span>🎓 빅데이터 석사 수련 중</span></div>
    <div class="rpg-lv">LEVEL <b>28</b> <small>— 성과 1건 = 1레벨. 직접 만든 것만 카운트.</small>
      <div class="xpbar"><i></i></div>
    </div>
  </div>
</div></div>
<p class="pixel-note">감으로 쓴 숫자는 없습니다. 모든 스탯은 성과 기록 28건의 역량 태그 빈도로 계산했습니다. 🎮</p>

<!-- ============ STATS ============ -->
<h3 class="sec">⚔️ 스탯</h3>
<div class="stat-grid" id="stats"></div>

<!-- ============ CLASS TREE ============ -->
<h3 class="sec">🧭 전직 트리</h3>
<div class="tree">
  <div class="node"><div class="yr">~2020</div><div class="jb">경영학도</div><div class="ds">컴퓨터공학 멀티클래스 — 전공자들 사이에서 평균 A로 부전공 획득</div></div>
  <div class="node"><div class="yr">2022–2025</div><div class="jb">공공 Data Keeper</div><div class="ds">KCA 3년 — 데이터 품질·개방·정책연구, RPA·클라우드 전환</div></div>
  <div class="node"><div class="yr">2025</div><div class="jb">AX Educator</div><div class="ds">KMA — KT AX 디그리 2.0 운영, 수강생 13,019명</div></div>
  <div class="node"><div class="yr">2026~</div><div class="jb">AX Consultant ★</div><div class="ds">MuniLabs — 에이전틱 시스템 설계·운용 + 석사 수련 병행</div></div>
</div>

<!-- ============ EQUIPMENT ============ -->
<h3 class="sec">🎒 장비</h3>
<div class="equip">
  <div class="eq legend"><div class="ic">🦾</div><div><div class="gr">LEGENDARY</div><div class="nm">Claude Code 하네스</div><div class="ds">블로그 발행·카드뉴스·위키 등 10+ 도메인 에이전트를 일상 운영 — 이 페이지도 산출물</div></div></div>
  <div class="eq epic"><div class="ic">🐍</div><div><div class="gr">EPIC</div><div class="nm">Python</div><div class="ds">예측모델(scikit-learn 앙상블)·K-Means 클러스터링·ARIMA 시계열·Optuna 튜닝</div></div></div>
  <div class="eq epic"><div class="ic">⚡</div><div><div class="gr">EPIC</div><div class="nm">Power Platform</div><div class="ds">Power Automate 피드백 993건 자동화, Copilot Studio·Power Apps, SharePoint 사이트 2개 구축</div></div></div>
  <div class="eq rare"><div class="ic">📊</div><div><div class="gr">RARE</div><div class="nm">Power BI · Tableau</div><div class="ds">VOC 품질 KPI·AX 절감시간 실시간 대시보드 구축, Tableau 부트캠프 수료</div></div></div>
  <div class="eq rare"><div class="ic">🗄️</div><div><div class="gr">RARE</div><div class="nm">SQL · DBeaver</div><div class="ds">SQLD 보유 — 개방 데이터 81건 품질진단·정비에 실전 사용</div></div></div>
  <div class="eq rare"><div class="ic">🎨</div><div><div class="gr">RARE</div><div class="nm">Figma · Vrew · GA4</div><div class="ds">AI 쇼츠 가이드 7편 제작, GA4 자격증(2026) — 콘텐츠·분석 보조 장비</div></div></div>
</div>

<!-- ============ TROPHIES ============ -->
<h3 class="sec">🏆 업적</h3>
<div class="trophy">
  <div class="tp"><div class="em">🏆</div><div class="tt">과기정통부 표창 (2024.12)</div><div class="ds">공공데이터 활성화 유공 — 데이터 품질·개방·연계 강화 성과로 수여</div></div>
  <div class="tp"><div class="em">🥇</div><div class="tt">평가 2년 연속 '우수' 등급</div><div class="ds">공공데이터 제공운영·데이터기반행정 실태점검, 기관 최초 — 품질관리 점수 만점</div></div>
  <div class="tp"><div class="em">💯</div><div class="tt">성과관리 수준진단 100점</div><div class="ds">전자정부 성과관리, 기관 최초 (2024) — 9개 시스템 총괄, 3년 연속 90점 이상</div></div>
  <div class="tp"><div class="em">📘</div><div class="tt">가이드북 다운로드 3만+</div><div class="ds">ChatGPT 업무활용 가이드북 2.0 집필·개정 총괄 — 교육영상 9건 별도 제작</div></div>
  <div class="tp"><div class="em">⏱️</div><div class="tt">연 9,392시간 절감</div><div class="ds">RPA 9건 구축·고도화 + 26억 규모 차세대 시스템 클라우드 전환 — 절감 인력 4명 신규사업 전환</div></div>
  <div class="tp"><div class="em">🎓</div><div class="tt">수강생 13,019명 교육 운영</div><div class="ds">KT AX 디그리 2.0 — 수료 6,124명, 전문가 심층 피드백 993건 지원</div></div>
  <div class="tp"><div class="em">📊</div><div class="tt">Kaggle Top 36%</div><div class="ds">대출상환 예측 AUC 0.92369 (1,324/3,724위) — CatBoost·LightGBM·XGBoost 앙상블 + Optuna</div></div>
  <div class="tp"><div class="em">🦥</div><div class="tt">자동화 연대기 연재 중</div><div class="ds">1주 1편, 직접 만들고 이해한 자동화만 기록 — 총 8편 계획</div></div>
</div>

<!-- ============ QUESTS ============ -->
<h3 class="sec">📜 퀘스트 로그</h3>
<div class="quest">
  <div class="q main"><span class="tag">MAIN</span><div><div class="qt">빅데이터 석사 논문</div><div class="qd">성균관대 빅데이터학과 (2025.03~) — 연구 주제 확정 단계, 일과 연구를 병행 중</div></div></div>
  <div class="q weekly"><span class="tag">WEEKLY</span><div><div class="qt">자동화 연대기 (2lazysodoit)</div><div class="qd">1주에 하나씩 직접 만든 자동화를 기록 — 출퇴근 개발환경, 교회 주보, 멀티채널 발행, 카드뉴스 등 총 8편 계획 → <a href="/categories/#자동화연대기">시리즈 보기</a></div></div></div>
  <div class="q side"><span class="tag">SIDE</span><div><div class="qt">Kaggle Playground</div><div class="qd">매 시즌 참여로 분석 스킬 단련 — 최근 대출상환 예측 Top 36%, 학생점수 예측 시즌 참여</div></div></div>
</div>

<div class="rpg-cta">파티 모집 중 — 자동화 아이디어, 협업, 강의 문의는 <a href="/profile/">텍스트 소개 · 연락처</a>에서. 🌿</div>

<script>
/* ===== stats: data-driven from achievements DB ===== */
(function(){
  var stats=[
    {nm:'문제정의·기획',en:'Problem Framing',lv:9,g:92,src:'성과 12건 — 약 20개 기관 분석과제 기획 컨설팅, 화장품 위해평가 B2B 모델 설계, AX 피드백 프로세스 기획 등',up:true},
    {nm:'데이터 분석',en:'Data Analysis',lv:8,g:84,src:'성과 9건 — 식수인원 예측모델(MAE 8.17·R² 0.85), 기상특보 시계열 분석(ARIMA), K-Means 클러스터링 2건, Kaggle AUC 0.924',up:true},
    {nm:'자동화·프로세스',en:'Automation',lv:8,g:80,src:'성과 7건 — RPA 9건 구축(연 9,392시간 절감·누적 1.3만건 처리), 수료증 발송 5배 가속, AI 쇼츠 제작 70% 단축',up:true},
    {nm:'AI·에이전틱',en:'AI & Agentic',lv:8,g:78,src:'성과 7건 — ChatGPT 가이드북 2.0(3만 DL), AI 기술기준 정립, 10+ 도메인 에이전트 하네스 운영 중',up:true},
    {nm:'프로젝트 관리',en:'Project Mgmt',lv:7,g:74,src:'성과 7건 — 26억 클라우드 전환 사업, 13,019명 교육 운영, 3년 유지보수 계약 관리(2.3억 절감)'},
    {nm:'보고서·문서화',en:'Documentation',lv:7,g:72,src:'성과 7건 — 정책보고서 2개년 발간, 가이드북 집필·개정, 12년 만의 내규 전부개정'},
    {nm:'커뮤니케이션',en:'Communication',lv:7,g:70,src:'성과 5건 — 개발자↔현업 요구사항 조율, 기관 간담회 11회, 인터뷰 영상 정리로 의견차 최소화'},
    {nm:'BI·시각화',en:'BI & Viz',lv:6,g:64,src:'성과 4건 — VOC 품질 Power BI 대시보드, AX 절감시간 실시간 대시보드(총 3,547분 추적)'}
  ];
  var wrap=document.getElementById('stats');if(!wrap)return;
  stats.forEach(function(s){
    var d=document.createElement('div');d.className='stat'+(s.up?' up':'');
    d.innerHTML='<div class="row"><span class="nm">'+s.nm+'<small>'+s.en+'</small></span>'+
      '<span class="lv">Lv.'+s.lv+'</span></div>'+
      '<div class="bar"><i data-g="'+s.g+'"></i></div>'+
      '<div class="src">근거: '+s.src+'</div>';
    wrap.appendChild(d);
  });
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.style.width=e.target.dataset.g+'%';io.unobserve(e.target);}
  });},{threshold:.4});
  wrap.querySelectorAll('.bar i').forEach(function(i){io.observe(i);});
})();
</script>
</div>
