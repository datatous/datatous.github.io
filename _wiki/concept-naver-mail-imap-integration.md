---
title: "네이버 메일 IMAP 연동 — 인증 강제와 인코딩 함정"
wiki_type: concept
tags: [imap, email-automation, python, authentication, encoding, gotcha]
last_modified_at: 2026-09-23
excerpt: "네이버 메일은 공개 API가 없고 기업용 NAVER WORKS Mail API는 개인 계정에 쓸 수 없어, IMAP이 프로그램으로 메일함에 접근하는 유일한 정식 경로다. 파이썬 표준 라이브러리 (`imaplib`, `email`)만으로 읽기 전용 연동을 구현할 수 있지만, ① 2025-06-24부터 강제된 2단계 인증 + 애플리케이션 비밀번호 정책과 ② I"
---

<span class="wiki-type-badge">concept</span>

## Summary

네이버 메일은 공개 API가 없고 기업용 NAVER WORKS Mail API는 개인 계정에 쓸 수 없어,
IMAP이 프로그램으로 메일함에 접근하는 유일한 정식 경로다. 파이썬 표준 라이브러리
(`imaplib`, `email`)만으로 읽기 전용 연동을 구현할 수 있지만, ① 2025-06-24부터
강제된 2단계 인증 + 애플리케이션 비밀번호 정책과 ② IMAP 프로토콜 자체가 안고 있는
한글 관련 인코딩 함정(폴더명, 검색어, 날짜 포맷) 두 층위를 모두 넘어야 한다.
[출처: sources/022-naver-mail-imap-technical-2026-09-23.md]

## Key Facts

- **공개 API 부재** — 네이버는 개인 메일용 공개 API가 없다. NAVER WORKS Mail API는
  기업(그룹웨어) 계정 전용이라 개인 `naver.com` 계정에는 쓸 수 없다. IMAP이 유일한
  정식 경로다. [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **앱 비밀번호 강제화** — 2025-06-24부터 POP3/IMAP/SMTP 접속에 2단계 인증 +
  애플리케이션 비밀번호가 필수가 됐다. 유예기간(11-18)이 끝난 뒤로는 일반 비밀번호로
  로그인 자체가 실패한다(`AUTHENTICATIONFAILED`). [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **단체(그룹) 아이디는 연동 불가** — 그룹 아이디는 애플리케이션 비밀번호 발급을
  지원하지 않아 IMAP 연동 경로 자체가 막힌다. [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **서버 정보** — IMAP `imap.naver.com:993`(SSL), SMTP `smtp.naver.com:587`(STARTTLS)
  또는 `:465`(SSL). 네이버 메일 환경설정에서 IMAP/SMTP 사용을 별도로 켜야 한다.
  [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **파이썬 표준 라이브러리만으로 구현 가능** — `imaplib` + `email` 모듈로 충분하고
  외부 패키지 설치가 필요 없다. [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **읽음 표시를 건드리지 않는 조합** — `select(mailbox, readonly=True)` + 본문 조회 시
  `FETCH ... BODY[]` 대신 `BODY.PEEK[]`. 둘 다 `/Seen` 플래그를 바꾸지 않는다. 실제로
  본문을 읽은 메일이 다른 클라이언트에서 "안 읽음"으로 남는 것을 확인했다.
  [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- 🔴 **한글 폴더명 함정** — IMAP은 폴더명을 modified UTF-7로 인코딩해 주고받는다
  (한글 폴더명이 `&zETGqQ-` 같은 형태로 전송됨). 파이썬 `imaplib`은 ASCII만 보낼 수
  있어 한글 폴더명을 그대로 넘기면 `UnicodeEncodeError`로 죽는다. **파이썬 표준
  라이브러리에는 modified UTF-7 코덱이 없어** 인코더/디코더를 직접 구현해야 한다.
  [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **한글 검색 함정** — 비-ASCII 검색어는 인라인으로 보낼 수 없고, `imap.literal`에
  UTF-8 바이트를 실어 `UID SEARCH CHARSET UTF-8 <criteria>` 형태로 보내야 한다. ASCII
  검색어는 인라인으로 충분하다. [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **SINCE 날짜 로케일 함정** — IMAP `SINCE`는 `DD-Mon-YYYY` 형식을 요구하는데, 파이썬
  `strftime`의 `%b`는 로케일을 타서 한국어 환경에서 "9월" 같은 문자열이 나와 규격에
  안 맞는다. 월 이름을 직접 테이블로 둬야 한다. [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]
- **`uid()`의 `None` 인자는 조용히 무시된다** — 조건부로 인자를 끼워 넣는 코드를
  분기 없이 짤 수 있다. [출처: sources/022-naver-mail-imap-technical-2026-09-23.md]

## Details

### 인증 정책 타임라인

| 시점 | 상태 |
|---|---|
| ~2025-06-23 | 일반 비밀번호로 IMAP/POP3/SMTP 로그인 가능 |
| 2025-06-24 | 2단계 인증 + 앱 비밀번호 필수화 발표, 유예기간 시작 |
| 2025-11-18 | 유예 종료 — 일반 비밀번호 로그인 완전 차단 |

그룹(단체) 아이디는 이 정책의 예외가 아니라 **애초에 앱 비밀번호 발급 메뉴 자체가
없어** 위 타임라인과 무관하게 연동이 불가능하다.

### 한글 폴더명 처리 패턴

modified UTF-7은 IMAP RFC 3501이 정의하는 폴더명 전용 인코딩이며, 표준 UTF-7과
미묘하게 다르다(패딩·구분자 규칙 차이). 파이썬 표준 라이브러리의 `encodings` 모듈에
UTF-7 코덱은 있어도 modified 버전은 없으므로, `list()`/`select()`/`create()` 등
폴더명을 다루는 모든 IMAP 명령 앞뒤에 인코더/디코더를 직접 끼워 사용자에게는 한글
이름을 그대로 노출하고, 와이어 프로토콜에서만 ASCII로 변환하는 계층을 둬야 한다.

### 일반화

이 두 함정(한글 폴더명 인코딩, 로케일 의존 날짜 포맷)은 네이버에 국한되지 않고
**한국어 메일함을 다루는 모든 IMAP 클라이언트 구현**에 공통 적용된다. RFC 표준
동작이 플랫폼 로케일이나 언어별 문자셋과 충돌하는 지점에서는, "표준을 따랐으니
될 것"이라는 가정이 깨지고 별도 변환 계층이 필요하다는 게 일반화 가능한 교훈이다.

## 함께 보기

- [[concept-mail-attachment-automation-constraint]] — 같은 이메일 자동화 도메인의
  다른 제약(Gmail MCP 첨부 다운로드 불가). 플랫폼마다 막히는 지점이 다르다는 대조
- [[concept-powershell-regex-text-pitfalls]] — 로케일·인코딩이 조용히 결과를
  틀리게 만드는 같은 계열의 함정
- [[entity-henry-agentic-system]] — 이 연동이 추가된 하네스
