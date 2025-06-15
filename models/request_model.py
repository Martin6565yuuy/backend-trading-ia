from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    symbol: str       # Ej: BTC/USDT, AAPL
    interval: str     # Ej: 1h, 4h, 1d
