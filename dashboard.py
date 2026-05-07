import gradio as gr

from api.quotes import get_quotes, crawl_category, add_favorite


def show_dashboard():
    quotes = get_quotes()

    if not quotes:
        return "데이터가 없습니다. 먼저 🌐 Data Crawling 탭에서 데이터를 수집하세요."

    total = len(quotes)
    authors = set(q["author"] for q in quotes)
    categories = set(q["category"] for q in quotes)
    moods = set(q["mood"] for q in quotes)

    return f"""
QuoteMind AI Dashboard

전체 명언 수: {total}
저자 수: {len(authors)}
카테고리 수: {len(categories)}
감정 유형 수: {len(moods)}
"""


def crawl_ui(category):
    if not category:
        return "카테고리를 입력하세요. 예: life, love, humor, truth, inspirational"

    return crawl_category(category)


def search_quotes(keyword, category):
    quotes = get_quotes()

    if not quotes:
        return "데이터가 없습니다. 먼저 크롤링하세요."

    result = ""

    for q in quotes:
        keyword_ok = True
        category_ok = True

        if keyword:
            keyword_ok = keyword.lower() in q["text"].lower() or keyword.lower() in q["author"].lower()

        if category:
            category_ok = category.lower() in q["category"].lower()

        if keyword_ok and category_ok:
            result += f"""
ID: {q["id"]}
명언: {q["text"]}
저자: {q["author"]}
카테고리: {q["category"]}
감정: {q["mood"]}
단어 수: {len(q["text"].split())}
------------------------------
"""

    if result == "":
        return "검색 결과가 없습니다."

    return result


def recommend_mood(mood):
    quotes = get_quotes()

    if not quotes:
        return "데이터가 없습니다. 먼저 크롤링하세요."

    result = ""

    for q in quotes:
        if q["mood"] == mood:
            result += f"{q['text']}\n- {q['author']}\n\n"

    if result == "":
        return "추천할 명언이 없습니다."

    return result


def analyze_quote(quote_id):
    quotes = get_quotes()

    for q in quotes:
        if q["id"] == int(quote_id):
            words = q["text"].split()
            longest = max(words, key=len)

            return f"""
명언:
{q["text"]}

저자: {q["author"]}
카테고리: {q["category"]}
감정: {q["mood"]}

단어 수: {len(words)}
글자 수: {len(q["text"])}
가장 긴 단어: {longest}
"""

    return "해당 ID의 명언이 없습니다."


def add_favorite_ui(quote_id):
    result = add_favorite(int(quote_id))
    return result["message"]


def project_report():
    return """
본 프로젝트는 FastAPI 기반의 QuoteMind AI 명언 추천 및 분석 시스템입니다.

quotes.toscrape.com 사이트에서 카테고리별 명언 데이터를 크롤링하고,
SQLite 데이터베이스에 저장하였습니다.

FastAPI를 사용하여 CRUD API를 구현하였고,
Swagger UI(/docs)를 통해 API 기능을 확인할 수 있도록 구성하였습니다.

또한 Gradio를 FastAPI에 mount하여 사용자 인터페이스를 제작하였습니다.
사용자는 명언 검색, 감정별 추천, 명언 분석, 즐겨찾기 기능을 사용할 수 있습니다.

특히 mood recommendation 기능을 추가하여
사용자의 상황에 맞는 명언을 추천할 수 있도록 하였습니다.
"""


def create_ui():
    with gr.Blocks(title="QuoteMind AI") as demo:
        gr.Markdown("# QuoteMind AI")
        gr.Markdown("FastAPI 기반 감정별 명언 추천 및 분석 시스템")

        with gr.Tab("📊 Dashboard"):
            btn = gr.Button("Load Dashboard")
            output = gr.Textbox(lines=8)
            btn.click(show_dashboard, outputs=output)

        with gr.Tab("🌐 Data Crawling"):
            category = gr.Textbox(label="Category", placeholder="life, love, humor, truth, inspirational")
            btn = gr.Button("Crawl Quotes")
            output = gr.Textbox()
            btn.click(crawl_ui, inputs=category, outputs=output)

        with gr.Tab("🔎 Smart Search"):
            keyword = gr.Textbox(label="Keyword", placeholder="Einstein, life, love...")
            category = gr.Textbox(label="Category", placeholder="life, love, humor...")
            btn = gr.Button("Search")
            output = gr.Textbox(lines=18)
            btn.click(search_quotes, inputs=[keyword, category], outputs=output)

        with gr.Tab("😊 Mood Recommendation"):
            mood = gr.Dropdown(
                choices=["motivation", "study", "love", "happy"],
                label="Mood"
            )
            btn = gr.Button("Recommend")
            output = gr.Textbox(lines=15)
            btn.click(recommend_mood, inputs=mood, outputs=output)

        with gr.Tab("📈 Quote Analyzer"):
            quote_id = gr.Number(label="Quote ID")
            btn = gr.Button("Analyze")
            output = gr.Textbox(lines=15)
            btn.click(analyze_quote, inputs=quote_id, outputs=output)

        with gr.Tab("⭐ Favorites"):
            quote_id = gr.Number(label="Quote ID")
            btn = gr.Button("Add Favorite")
            output = gr.Textbox()
            btn.click(add_favorite_ui, inputs=quote_id, outputs=output)

        with gr.Tab("📝 Project Report"):
            btn = gr.Button("Show Report")
            output = gr.Textbox(lines=18)
            btn.click(project_report, outputs=output)

    return demo