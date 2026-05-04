from decimal import Decimal, ROUND_HALF_UP


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

def power(a, b):
    return a ** b


receita = 100,000

impostos = 10,000

custos  = 50,000

despesa_variáveis = 5,000

resultado = receita - impostos - custos - despesa_variáveis

-- Variáveis --

ICMS = 3.60%
PIS = 1.65%
COFINS = 9.25%
IPI = 5.00%
DIFAL_ICMS = 6.00%

lucro_desejado = 50.00%

fator_liquido_sem_ipi = 1 - (ICMS + PIS + COFINS + DIFAL_ICMS + lucro_desejado)

-- Preço de venda --

custo_base = 

preco_venda_sem_ipi = custo_base / fator_liquido_sem_ipi

valor_ipi = preco_venda_sem_ipi * IPI

preco_venda_com_ipi = preco_venda_sem_ipi + valor_ipi

lucro_estimado = preco_venda_sem_ipi * lucro_desejado






