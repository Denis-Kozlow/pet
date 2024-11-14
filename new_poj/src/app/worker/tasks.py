from src.app.repository.repository import add_package
from src.app.worker.celery_config import celery_app


@celery_app.task(
    bind=True,
    acks_late=True,
    max_reties=10,
    default_retry_delay=60,
)
def add_package_broker(self, data):
    try:
        add_package(data)
    except ConnectionError:
        self.retry()
        return "ConnectionError"
    except Exception:
        print("Exception")
        self.retry()
    return 200
