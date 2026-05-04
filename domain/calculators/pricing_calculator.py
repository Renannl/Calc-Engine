from decimal import Decimal
from dataclasses import dataclass

from shared.utils.money import money


@dataclass
class PricingInput:
    custo_base: Decimal
    icms: Decimal
    pis: Decimal
    cofins: Decimal
    ipi: Decimal
    difal_icms: Decimal
    lucro_desejado: Decimal


@dataclass
class PricingResult:
    preco_venda_sem_ipi: Decimal
    valor_ipi: Decimal
    preco_venda_com_ipi: Decimal
    lucro_estimado: Decimal


class PricingCalculator:

    @staticmethod
    def _validate_input(data: PricingInput):

        if data.custo_base <= 0:
            raise ValueError(
                "Custo base deve ser maior que zero"
            )

        percentages = {
            "ICMS": data.icms,
            "PIS": data.pis,
            "COFINS": data.cofins,
            "IPI": data.ipi,
            "DIFAL_ICMS": data.difal_icms,
            "LUCRO": data.lucro_desejado,
        }

        for field, value in percentages.items():

            if value < 0:
                raise ValueError(
                    f"{field} não pode ser negativo"
                )

            if value > 1:
                raise ValueError(
                    f"{field} não pode ser maior que 100%"
                )

    @staticmethod
    def _calculate_net_factor(
        data: PricingInput
    ) -> Decimal:

        factor = Decimal("1") - (
            data.icms
            + data.pis
            + data.cofins
            + data.difal_icms
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
            preco_venda_sem_ipi * data.ipi
        )

        preco_venda_com_ipi = money(
            preco_venda_sem_ipi + valor_ipi
        )

        lucro_estimado = money(
            preco_venda_sem_ipi * data.lucro_desejado
        )

        return PricingResult(
            preco_venda_sem_ipi=preco_venda_sem_ipi,
            valor_ipi=valor_ipi,
            preco_venda_com_ipi=preco_venda_com_ipi,
            lucro_estimado=lucro_estimado,
        )