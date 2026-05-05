from decimal import Decimal

from pydantic import BaseModel


class PricingRequest(BaseModel):
    custo_base: Decimal
    lucro_desejado: Decimal


class PricingResponse(BaseModel):
    preco_venda_sem_ipi: Decimal
    valor_ipi: Decimal
    preco_venda_com_ipi: Decimal
    lucro_estimado: Decimal
    lucro_porcentagem: Decimal
    preco_venda_com_icms: Decimal