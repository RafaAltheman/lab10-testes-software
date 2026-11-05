CUPONS = {
    "DEZ": (10, 10000),
    "VINTE": (20, 30000)
}


class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._cupom = None

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")

        if type(quantidade) is not int or quantidade < 1:
            raise ValueError("quantidade invalida")

        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")

        self._cupom = codigo

    @property
    def total(self):
        desconto = 0

        if self._cupom is not None:
            porcentagem, minimo = CUPONS[self._cupom]

            if self._subtotal >= minimo:
                desconto = porcentagem

        return self._subtotal * (100 - desconto) // 100
