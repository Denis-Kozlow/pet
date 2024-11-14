from redis import StrictRedis
from redis_cache import RedisCache
from src.app.config.config import settings


redis_client = StrictRedis(
    settings.REDIS_HOST, decode_responses=True)
cache = RedisCache(redis_client=redis_client)
