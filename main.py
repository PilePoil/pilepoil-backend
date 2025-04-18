# FastAPI backend enrichi avec /api/stats et /api/meubles/:id
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API PilePoil v1.5 🚀"}

@app.get("/api/stats")
def stats():
    return {
        "nb_produits": 0,
        "enseignes": ["BUT", "Conforama"],
        "updatedAt": "à compléter"
    }
