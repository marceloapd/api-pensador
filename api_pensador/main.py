from fastapi import FastAPI
from .routes.get_phrases import router as get_phrases

app = FastAPI()


app.include_router(get_phrases)