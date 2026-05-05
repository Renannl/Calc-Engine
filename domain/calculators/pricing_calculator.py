from decimal import Decimal
from dataclasses import dataclass
from shared.utils.money import money
from domain.constants.tax_rates import (
    ICMS,
    PIS,
    COFINS,
    IPI,
    DIFAL_ICMS,
)


@dataclass
class PricingInput:
    custo_base: Decimal
    lucro_desejado: Decimal


@dataclass
class PricingResult:
    preco_venda_sem_ipi: Decimal
    valor_ipi: Decimal
    preco_venda_com_ipi: Decimal
    preco_venda_com_icms: Decimal
    lucro_estimado: Decimal
    lucro_porcentagem: Decimal


class PricingCalculator:

    @staticmethod
    def _validate_input(data: PricingInput):

        if data.custo_base <= 0:
            raise ValueError(
                "Custo base deve ser maior que zero"
            )

        if data.lucro_desejado < 0:
            raise ValueError(
                "Lucro desejado não pode ser negativo"
            )

        if data.lucro_desejado > 1:
            raise ValueError(
                "Lucro desejado não pode ser maior que 100%"
            )

    @staticmethod
    def _calculate_net_factor(
        data: PricingInput
    ) -> Decimal:

        factor = Decimal("1") - (
            ICMS
            + PIS
            + COFINS
            + DIFAL_ICMS
            + data.lucro_desejado
        )

        if factor <= 0:
            raise ValueError(
                "A soma dos percentuais não pode ser maior ou igual a 100%"
            )

        return factor

    @staticmethod
    def calculate(
        data: PricingInput
    ) -> PricingResult:

        PricingCalculator._validate_input(data)

        fator_liquido_sem_ipi = (
            PricingCalculator._calculate_net_factor(data)
        )

        preco_venda_sem_ipi = money(
            data.custo_base / fator_liquido_sem_ipi
        )

        valor_ipi = money(
            preco_venda_sem_ipi * IPI
        )

        preco_venda_com_ipi = money(
            preco_venda_sem_ipi + valor_ipi
        )

        preco_venda_com_icms = money(
            preco_venda_sem_ipi * ICMS
        )

        lucro_estimado = money(
            preco_venda_sem_ipi * data.lucro_desejado
        )

        lucro_porcentagem = money(
            lucro_estimado / data.custo_base
        )
        

        return PricingResult(
            preco_venda_sem_ipi=preco_venda_sem_ipi,
            valor_ipi=valor_ipi,
            preco_venda_com_ipi=preco_venda_com_ipi,
            lucro_estimado=lucro_estimado,
            lucro_porcentagem=lucro_porcentagem,
            preco_venda_com_icms=preco_venda_com_icms
        )