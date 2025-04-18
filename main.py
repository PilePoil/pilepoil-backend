# FastAPI backend enrichi avec /api/stats et /api/meubles/:id
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from PilePoil"}
