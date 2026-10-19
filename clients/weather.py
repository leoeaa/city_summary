from clients.http import get_json, NotFound, AppError

CODES = CODES = {
    0: "ясно", 
    1: "преимущественно ясно", 
    2: "переменная облачность", 
    3: "пасмурно",
    45: "туман", 
    48: "туман с изморозью", 
    51: "слабая морось", 
    53: "морось",
    55: "сильная морось", 
    61: "небольшой дождь", 
    63: "дождь", 
    65: "сильный дождь",
    71: "небольшой снег", 
    73: "снег", 
    75: "сильный снег", 
    80: "небольшой ливень",
    81: "ливень", 
    82: "сильный ливень", 
    95: "гроза",
    96: "гроза с градом", 
    99: "сильная гроза с градом"
}

def get_weather(city):
    geo = get_json("https://geocoding-api.open-meteo.com/v1/search",
                   { "name": city, "count": 1})
    results = geo.get("results") or []
    if not results:
        raise NotFound(city)
    shi, dol = results[0]["latitude"], results[0]["longitude"]
    x_y = get_json("https://api.open-meteo.com/v1/forecast",
                 {"latitude": shi,"longitude": dol,"current": "temperature_2m,weather_code"})
    current = x_y.get("current") or {}
    if "temperature_2m" not in current or "weather_code" not in current:
        raise AppError("Ошибка в получении температуры или погоды")
    return {"temp_c": current["temperature_2m"], "description": CODES.get(current["weather_code"], "unknown")}