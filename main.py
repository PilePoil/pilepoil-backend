from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# Connexion MongoDB à partir de la variable d'environnement
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client["pilepoil"]
collection = db["meubles"]

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API PilePoil v1.5 🚀"}

@app.get("/api/stats")
def get_stats():
    count = collection.count_documents({})
    enseignes = collection.distinct("enseigne")
    return {
        "nb_produits": count,
        "enseignes": enseignes,
    }

@app.get("/api/meubles/{meuble_id}")
def get_meuble(meuble_id: str):
    from bson.objectid import ObjectId
    meuble = collection.find_one({"_id": ObjectId(meuble_id)})
    if meuble:
        meuble["_id"] = str(meuble["_id"])
        return meuble
    return {"error": "Meuble non trouvé"}
