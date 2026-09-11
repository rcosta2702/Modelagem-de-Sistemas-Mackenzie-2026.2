"""Regras de frete; premissas não especificadas estão em IMPLEMENTACAO.md."""

import re
from decimal import Decimal, InvalidOperation


FRETE_PADRAO = Decimal("20.00")
FAIXAS_REGIONAIS = (
    (1000000, 39999999, "Sudeste"),
    (40000000, 65999999, "Nordeste"),
    (66000000, 69999999, "Norte"),
    (70000000, 76799999, "Centro-Oeste"),
    (76800000, 77999999, "Norte"),
    (78000000, 79999999, "Centro-Oeste"),
    (80000000, 99999999, "Sul"),
)


def identificar_regiao(cep):
    """Identifica a região pela faixa postal, sem consultar endereços externos."""
    if not isinstance(cep, str) or not re.fullmatch(r"[0-9]{5}-?[0-9]{3}", cep):
        raise ValueError("CEP inválido ou região não atendida")
    numero = int(cep.replace("-", ""))
    for inicio, fim, regiao in FAIXAS_REGIONAIS:
        if inicio <= numero <= fim:
            return regiao
    raise ValueError("CEP inválido ou região não atendida")


def calcular_frete(valor_carrinho, cep):
    """Retorna região e frete; valores inválidos geram ValueError."""
    try:
        valor = Decimal(str(valor_carrinho))
    except (InvalidOperation, ValueError):
        raise ValueError("Valor do carrinho inválido") from None
    if not valor.is_finite() or valor <= 0:
        raise ValueError("Valor do carrinho inválido")

    regiao = identificar_regiao(cep)
    limite = Decimal("300.00") if regiao == "Norte" else Decimal("200.00")
    frete = Decimal("0.00") if valor >= limite else FRETE_PADRAO
    return {"regiao": regiao, "frete": float(frete)}
