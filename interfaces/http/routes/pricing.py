from fastapi import APIRouter

from domain.calculators.pricing_calculator import (
    PricingCalculator,
    PricingInput,
)

from interfaces.http.schemas.pricing import (
    PricingRequest,
    PricingResponse,
)


router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"],
)


@router.post(
    "/calculate",
    response_model=PricingResponse,
)
def calculate_pricing(
    request: PricingRequest,
):

    data = PricingInput(
        custo_base=request.custo_base,
        lucro_desejado=request.lucro_desejado,
    )

    result = PricingCalculator.calculate(data)

    return PricingResponse(
        preco_venda_sem_ipi=result.preco_venda_sem_ipi,
        valor_ipi=result.valor_ipi,
        preco_venda_com_ipi=result.preco_venda_com_ipi,
        lucro_estimado=result.lucro_estimado,
        lucro_porcentagem=result.lucro_porcentagem,
        preco_venda_com_icms=result.preco_venda_com_icms,
    )