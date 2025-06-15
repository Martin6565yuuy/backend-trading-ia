from utils.technical import get_technical_indicators

def analyze_market(symbol: str, interval: str):
    indicators = get_technical_indicators(symbol, interval)

    recommendation = "wait"
    if indicators["RSI"] < 30:
        recommendation = "buy"
    elif indicators["RSI"] > 70:
        recommendation = "sell"

    return {
        "symbol": symbol,
        "interval": interval,
        "indicators": indicators,
        "recommendation": recommendation
    }
