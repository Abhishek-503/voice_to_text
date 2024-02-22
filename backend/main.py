from api.endpoints import audio_to_text, sentiment_analysis, jokes, news
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
# from mangum import Mangum
import logging

app = FastAPI()
# handler = Mangum(app)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.info("Initializing all the EndPoints")


@app.get("/", include_in_schema=False)
def index():
    return "To access the APIs, Please add '/docs' at the end of the URL."


app.include_router(audio_to_text.router, prefix="")
app.include_router(sentiment_analysis.router, prefix="")
app.include_router(jokes.router, prefix="")
app.include_router(news.router, prefix="")
