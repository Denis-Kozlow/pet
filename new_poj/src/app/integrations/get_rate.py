import requests
from src.app.config.redis_client import cache
from src.app.config.config import settings
URL = settings.URLRATE
TTL = settings.TTLCACHE


@cache.cache(ttl=TTL, namespace="rate")
def get_rate(url: str = URL):
    res = requests.get(url)
    return res.json()
