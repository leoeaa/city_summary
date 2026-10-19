import time 
from clients.http import get_json, NotFound

cache = {}

def get_rate(x):
    t = time.time()
    if x in cache and cache[x][1] > t:
        return cache[x][0]
    data = get_json(f"https://api.frankfurter.dev/v2/rate/{x}/RUB")
    rate = data.get("rate")
    if rate is None:
        raise NotFound(f"currency {x}")
    cache[x] = (rate, t+300)
    return rate