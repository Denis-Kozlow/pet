from contextlib import nullcontext as does_not_raise
from pytest import mark, raises
from src.app.logic.calc import price_delivery
from decimal import Decimal


@mark.parametrize(
    "weight, cost, rate, result, expectation",
    [
        (245, 145.24, 91.23, round(Decimal(12500.700), 3), does_not_raise()),
        (532, 1231.242, 30.93, round(Decimal(12035.612), 3), does_not_raise()),
        (1, 1, 1, 1, raises(AssertionError)),
    ]
)
def test_price(weight, cost, rate, result, expectation):
    with expectation:
        assert price_delivery(weight, cost, rate,) == result
