from fastapi import APIRouter
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

from core.database import connect_db, create_table

router = APIRouter()


class Quote(BaseModel):
    text: str
    author: str
    category: str


def detect_mood(text, category):
    text = text.lower()
    category = category.lower()

    if "love" in text or category == "love":
        return "love"
    if "laugh" in text or "funny" in text or category == "humor":
        return "happy"
    if "success" in text or "dream" in text or category == "inspirational":
        return "motivation"
    if "life" in text or category in ["life", "truth"]:
        return "study"

    return "motivation"


def crawl_category(category):
    create_table()

    url = f"https://quotes.toscrape.com/tag/{category}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quote_items = soup.select(".quote")[:20]

    conn = connect_db()
    cur = conn.cursor()

    count = 0

    for item in quote_items:
        text = item.select_one(".text").get_text()
        author = item.select_one(".author").get_text()
        mood = detect_mood(text, category)

        cur.execute("""
            INSERT INTO quotes (text, author, category, mood)
            VALUES (?, ?, ?, ?)
        """, (text, author, category, mood))

        count += 1

    conn.commit()
    conn.close()

    return f"{category} 카테고리에서 {count}개의 명언을 저장했습니다."


@router.post("/crawl/{category}")
def crawl_quotes(category: str):
    message = crawl_category(category)
    return {"message": message}


@router.get("/quotes")
def get_quotes():
    create_table()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM quotes")
    rows = cur.fetchall()

    conn.close()

    return [dict(row) for row in rows]


@router.get("/quotes/{quote_id}")
def get_quote(quote_id: int):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM quotes WHERE id=?", (quote_id,))
    row = cur.fetchone()

    conn.close()

    if row:
        return dict(row)

    return {"message": "해당 명언이 없습니다."}


@router.post("/quotes")
def create_quote(quote: Quote):
    mood = detect_mood(quote.text, quote.category)

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO quotes (text, author, category, mood)
        VALUES (?, ?, ?, ?)
    """, (quote.text, quote.author, quote.category, mood))

    conn.commit()
    conn.close()

    return {"message": "명언이 추가되었습니다."}


@router.put("/quotes/{quote_id}")
def update_quote(quote_id: int, quote: Quote):
    mood = detect_mood(quote.text, quote.category)

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        UPDATE quotes
        SET text=?, author=?, category=?, mood=?
        WHERE id=?
    """, (quote.text, quote.author, quote.category, mood, quote_id))

    conn.commit()
    conn.close()

    return {"message": "명언이 수정되었습니다."}


@router.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM quotes WHERE id=?", (quote_id,))

    conn.commit()
    conn.close()

    return {"message": "명언이 삭제되었습니다."}


@router.post("/favorite/{quote_id}")
def add_favorite(quote_id: int):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO favorites (quote_id) VALUES (?)", (quote_id,))

    conn.commit()
    conn.close()

    return {"message": "즐겨찾기에 추가되었습니다."}