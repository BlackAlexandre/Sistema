def formatar_reais(valor):
    """
    Exemplo: 8500 vira R$ 8.500,00.
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
