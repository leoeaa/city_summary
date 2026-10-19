# Сводка по городу

## Установка
pip install -r requirements.txt

## Запуск
python main.py --city Moscow
python main.py --city Moscow --currency EUR
python main.py --city Moscow --json

## Коды выхода
0 - успех
2 - ошибка аргументов (argparse)
3 - город или код валюты не найден
4 - внешний сервис недоступен после повторов

## Особенности
timeout 10 с, до 3 повторов на Timeout / ConnectionError / 5xx / 429
кэш курса 5 минут
флаг --json