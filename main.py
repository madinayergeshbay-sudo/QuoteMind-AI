from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gradio as gr
import uvicorn
import os

from core.database import create_table
from api.quotes import router as quote_router
from ui.dashboard import create_ui

app = FastAPI(
    title="QuoteMind AI",
    description="FastAPI 기반 감정별 명언 추천 및 분석 시스템",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_table()

app.include_router(quote_router)

demo = create_ui()
app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))