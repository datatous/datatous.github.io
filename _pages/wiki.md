---
title: "Wiki — 세컨브레인"
permalink: /wiki/
layout: single
author_profile: false
sidebar:
  nav: "wiki"
header:
  overlay_image: /assets/images/header-banner.png
  overlay_filter: 0.35
excerpt: "공부하고, 만들고, 이해한 것들을 실시간으로 쌓는 지식 창고.<br>Henry의 에이전틱 시스템이 자동으로 관리합니다."
---

내 로컬 에이전틱 시스템의 **LLM Wiki**가 이곳으로 동기화된다. 읽은 아티클, 직접 구현하며 이해한 개념, 도구 분석을 출처와 함께 정리한다. 페이지는 삭제되지 않고 계속 업데이트된다.

{% assign type_names = "concept|Concepts|개념,entity|Entities|도구·시스템,topic|Topics|토픽,project|Projects|프로젝트,event|Events|이벤트" | split: "," %}
{% for tn in type_names %}
{% assign parts = tn | split: "|" %}
{% assign docs = site.wiki | where: "wiki_type", parts[0] | sort: "last_modified_at" | reverse %}
{% if docs.size > 0 %}

## {{ parts[1] }} <small>· {{ parts[2] }}</small>

<div class="entries-list">
{% for doc in docs %}
<div class="archive__item">
  <h3 class="archive__item-title" style="margin-bottom:0.3em;"><a href="{{ doc.url | relative_url }}">{{ doc.title }}</a></h3>
  <p class="archive__item-excerpt" style="margin:0;">{{ doc.excerpt | strip_html | truncate: 120 }}</p>
  <p class="archive__item-excerpt" style="margin:0.4em 0 0;"><small>업데이트 {{ doc.last_modified_at | date: "%Y-%m-%d" }}{% if doc.tags %} · {{ doc.tags | join: ", " }}{% endif %}</small></p>
</div>
{% endfor %}
</div>
{% endif %}
{% endfor %}

{% assign total = site.wiki | size %}
{% if total == 0 %}
> 아직 동기화된 위키 페이지가 없습니다.
{% endif %}
