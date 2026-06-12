# datatous.github.io

Henry의 자동화 연대기 — **2lazysodoit** 프로젝트. 1주에 하나씩, 직접 만들고 이해한 업무 자동화를 기록하는 블로그.

[Jekyll](https://jekyllrb.com/) + [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) (remote_theme) 기반.

## 로컬 미리보기

```bash
bundle install
bundle exec jekyll serve
```

http://localhost:4000 에서 확인.

## 새 글 추가

`_posts/YYYY-MM-DD-제목.md` 형식으로 파일을 추가하고 front matter를 채운다.

```yaml
---
title: "제목"
date: YYYY-MM-DD
categories:
  - 자동화연대기
tags:
  - 태그1
  - 태그2
header:
  teaser: /assets/images/posts/xxx.png
excerpt: "한 줄 요약"
---
```

## 배포

GitHub Pages가 `main` 브랜치를 자동 빌드/배포한다. 저장소 이름이 `<username>.github.io`이므로 별도 설정 없이 `https://datatous.github.io`에서 바로 서비스된다.
