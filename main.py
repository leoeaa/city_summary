import argparse, json, sys
from clients.http import AppError, NotFound
from processing.service import build_city_summary

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--city", required=True)
    p.add_argument("--currency", default="USD")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    try:
        s = build_city_summary(a.city, a.currency.upper())
    except NotFound as e:
        print(f"Не найдено: {e}", file=sys.stderr); return 3
    except AppError as e:
        print(f"Сервис недоступен: {e}", file=sys.stderr); return 4

    if a.json:
        print(json.dumps(s, ensure_ascii=False, indent=2))
    else:
        print(f"Город: {s['city']}")
        print(f"Погода: {s['weather']['temp_c']}°C, {s['weather']['description']}")
        print(f"Тёплая одежда: {'да' if s['weather']['warm_clothes'] else 'нет'}")
        print(f"{s['rates']['currency']}→RUB: {s['rates']['rate_to_rub']}")
        print(f"Дорогой курс: {'да' if s['rates']['expensive'] else 'нет'}")
    return 0

if __name__ == "__main__":
    sys.exit(main())