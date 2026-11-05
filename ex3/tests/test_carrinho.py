from carrinho import Carrinho


def test_dez_abaixo_minimo():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")

    assert c.total == 5000


def test_dez_no_minimo():
    c = Carrinho()
    c.adicionar(10000)
    c.aplicar_cupom("DEZ")
    assert c.total == 9000
