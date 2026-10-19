import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class AppError(Exception): pass
class NotFound(AppError): pass

retry = Retry(
    total=3,
    backoff_factor=1, 
    status_forcelist=[500, 502, 503, 504, 429],
    raise_on_status=False,
    allowed_methods=["GET"],
    respect_retry_after_header=True,
)

session = requests.Session()
session.mount("https://", HTTPAdapter(max_retries=retry))

def get_json(url, params=None):
    try:
        res = session.get(url, params=params, timeout=10)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        raise AppError(str(e)) from e
    if res.status_code == 404:
        raise NotFound(res.status_code)
    if not res.ok:
        raise AppError(res.status_code)
    try:
        return res.json()
    except ValueError as e:
        raise AppError("Ошибка в json") from e