from fastapi import FastAPI, Request
from models.request_model import AnalysisRequest
from service.analysis import analyze_market
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS (para permitir conexión desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # más adelante cambia esto por el dominio de tu web
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Servidor funcionando correctamente"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/analyze")
def analyse(request: AnalysisRequest):
    result = analyze_market(request.symbol, request.interval)
    return result

    # 🔧 Aquí iría el análisis con IA más adelante
    return {
        "activo": activo,
        "temporalidad": temporalidad,
        "recomendacion": "🔍 Análisis simulado: espera confirmación antes de entrar al mercado."
    }
