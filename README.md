# QuoteMind AI

FastAPI 기반 감정별 명언 추천 및 분석 시스템

---

## 배포 URL

- Dashboard: https://quote-mind-ai--madinayergeshba.replit.app
- Swagger API Docs: https://quote-mind-ai--madinayergeshba.replit.app/docs
- GitHub Repository: https://github.com/madinayergeshbay-sudo/QuoteMind-AI

---

## 프로젝트 소개

QuoteMind AI는 quotes.toscrape.com 사이트에서 명언 데이터를 수집하고,
SQLite 데이터베이스에 저장한 뒤 FastAPI와 Gradio를 활용하여
명언을 검색, 분석, 추천할 수 있도록 만든 웹 기반 프로젝트입니다.

이 프로젝트는 단순히 데이터를 보여주는 것이 아니라,
카테고리별 명언 수집, 키워드 검색, 감정별 추천, 명언 분석,
즐겨찾기 기능을 하나의 서비스로 구성한 시스템입니다.

---

## 주요 기능

### 📊 Dashboard
- 전체 명언 수 확인
- 저자 수 확인
- 카테고리 수 확인
- 감정 유형 수 확인

### 🌐 Data Crawling
- quotes.toscrape.com에서 명언 데이터 수집
- 카테고리별 명언 저장
- SQLite 데이터베이스 저장

### 🔎 Smart Search
- 키워드 기반 명언 검색
- 저자 이름 검색
- 카테고리 필터 검색

### 😊 Mood Recommendation
- motivation, study, love, happy 감정별 추천
- 사용자의 상황에 맞는 명언 제공

### 📈 Quote Analyzer
- 명언 ID 기반 분석
- 단어 수 분석
- 글자 수 분석
- 가장 긴 단어 확인

### ⭐ Favorites
- 마음에 드는 명언 즐겨찾기 저장

---

## 기술 스택

| 구분 | 사용 기술 |
|---|---|
| Backend | FastAPI |
| Frontend | Gradio |
| Database | SQLite3 |
| Crawling | BeautifulSoup4, requests |
| Visualization | matplotlib |
| Deploy | Replit |
| Language | Python |

---

## 프로젝트 구조

```bash
QuoteMind-AI/
├── main.py
├── requirements.txt
├── quotes.db
├── database.py
├── quotes.py
├── dashboard.py
├── charts.py
└── README.md
