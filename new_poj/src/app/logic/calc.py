from uuid import uuid4
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(f"{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def unique_id():
    return str(uuid4())


def price_delivery(weight, cost, rate):
    logger.info(f"weigh={weight}, cost={cost}, rate={rate}")
    res = (Decimal(weight) * Decimal(0.5) +
           Decimal(cost) * Decimal(0.1)) * Decimal(rate)
    logger.info(f"result={res}")
    return round(res, 3)
