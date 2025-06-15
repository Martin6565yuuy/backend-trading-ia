from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.request_model import AnalysisRequest
from services.analysis import analyze_market   # ← ojo: “services”, no “service”

app = FastAPI()

# ­CORS: deja abierto mientras pruebas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/analyze")
def analyze(request: AnalysisRequest):
    """
    Recibe JSON como:
    {
      "symbol": "BTC/USDT",
      "interval": "1h"
    }
    """
    result = analyze_market(request.symbol, request.interval)
    return result
