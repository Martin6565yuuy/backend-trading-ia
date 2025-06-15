from fastapi import FastAPI, Request
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

@app.post("/analizar")
async def analizar(request: Request):
    data = await request.json()
    activo = data.get("activo")
    temporalidad = data.get("temporalidad")

    # 🔧 Aquí iría el análisis con IA más adelante
    return {
        "activo": activo,
        "temporalidad": temporalidad,
        "recomendacion": "🔍 Análisis simulado: espera confirmación antes de entrar al mercado."
    }
