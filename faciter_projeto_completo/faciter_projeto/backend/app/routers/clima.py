import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/clima", tags=["Integração externa"])

@router.get("/{cidade}")
def clima(cidade: str):
    # Geocoding público do Open-Meteo: a API externa é chamada pelo backend.
    try:
        geo = httpx.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": cidade, "count": 1, "language": "pt", "format": "json"}, timeout=8).json()
        if not geo.get("results"): raise HTTPException(404, "Cidade não encontrada")
        loc = geo["results"][0]
        weather = httpx.get("https://api.open-meteo.com/v1/forecast", params={"latitude": loc["latitude"], "longitude": loc["longitude"], "current": "temperature_2m,weather_code", "timezone": "auto"}, timeout=8).json()
        return {"cidade": loc["name"], "temperatura": weather["current"]["temperature_2m"], "codigo_clima": weather["current"]["weather_code"]}
    except HTTPException: raise
    except Exception:
        raise HTTPException(502, "Não foi possível consultar o serviço de clima")
