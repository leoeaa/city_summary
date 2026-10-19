from clients.weather import get_weather
from clients.rates import get_rate
from processing.preprocessing import warm_clothes, expensive

def build_city_summary(city, currency="USD"):
    w = get_weather(city)
    r = get_rate(currency)
    
    return {
        "city": city,
        "weather": {
            "temp_c": w["temp_c"],
            "description": w["description"],
            "warm_clothes": warm_clothes(w["temp_c"])
        },
        "rates": {
            "currency": currency,
            "rate_to_rub": r,
            "expensive": expensive(r)
        }
    }