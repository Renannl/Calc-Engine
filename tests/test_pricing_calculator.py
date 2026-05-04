from decimal import Decimal
import pytest

from domain.calculators.pricing_calculator import (
    PricingCalculator,
    PricingInput,
)


def make_valid_input(**overrides):

    data = {
        "custo_base": Decimal("108.9"),
        "icms": Decimal("0.036"),
        "pis": Decimal("0.0165"),
        "cofins": Decimal("0.0925"),
        "ipi": Decimal("0.05"),
        "difal_icms": Decimal("0.06"),
        "lucro_desejado": Decimal("0.50"),
    }

    data.update(overrides)

    return PricingInput(**data)


def test_should_calculate_price_correctly():

    data = make_valid_input()

    result = PricingCalculator.calculate(data)

    assert result.preco_venda_sem_ipi == Decimal("369.15")