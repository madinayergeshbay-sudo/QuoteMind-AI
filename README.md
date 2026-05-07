# QuoteMind AI

FastAPI 기반 감정별 명언 추천 및 분석 시스템

---

## 프로젝트 소개

QuoteMind AI는 quotes.toscrape.com 사이트에서 명언 데이터를 수집하고,
사용자의 감정에 맞는 명언을 추천하는 AI 기반 명언 분석 시스템입니다.

본 프로젝트는 FastAPI, Gradio, SQLite를 활용하여 개발되었으며,
명언 검색, 감정 분석, 추천 시스템, 즐겨찾기 기능 등을 제공합니다.

---

## 주요 기능

### 🌐 Data Crawling
- 카테고리별 명언 데이터 수집
- SQLite 데이터베이스 저장

### 🔎 Smart Search
- 저자 검색
- 명언 검색
- 카테고리 검색

### 😊 Mood Recommendation
- 감정 기반 명언 추천
- 행복 / 슬픔 / 분노 / 동기부여 분석

### 📊 Quote Analyzer
- 명언 통계 분석
- 카테고리별 데이터 시각화

### ⭐ Favorites
- 즐겨찾기 저장 기능

---

## 프로젝트 구조

```bash
QuoteMind-AI
│
├── main.py
├── requirements.txt
├── quotes.py
├── database.py
├── charts.py
├── dashboard.py
├── quotes.db
└── readme.md
