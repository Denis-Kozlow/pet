from celery import Celery
from src.app.config.config import settings


celery_app = Celery("tasks")

celery_app.conf.update(
    broker_url=f'pyamqp://guest@{settings.RABBIT_HOST}//',
    broker_connection_retry_on_startup=True,
)

celery_app.autodiscover_tasks(['src.app.worker'])
