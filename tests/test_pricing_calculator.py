from decimal import Decimal
import pytest

from domain.calculators.pricing_calculator import (
    PricingCalculator,
    PricingInput,
)


def make_valid_input(**overrides):

    data = {
        "custo_base": Decimal("108.9"),
        "lucro_desejado": Decimal("0.79"),
    }

    data.update(overrides)

    return PricingInput(**data)


def test_should_calculate_price_correctly():

    data = make_valid_input()

    result = PricingCalculator.calculate(data)

    assert result.preco_venda_sem_ipi == Decimal("21780.00")
    assert result.valor_ipi == Decimal("1089.00")
    assert result.preco_venda_com_ipi == Decimal("22869.00")
    assert result.preco_venda_com_icms == Decimal("784.08")
    assert result.lucro_estimado == Decimal("17206.20")
    assert result.lucro_porcentagem == Decimal("158.00")