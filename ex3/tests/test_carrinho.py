import pytest
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


def test_vinte_no_minimo():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("VINTE")
    assert c.total == 24000


def test_vinte_abaixo_minimo():
    c = Carrinho()
    c.adicionar(29999)
    c.aplicar_cupom("VINTE")
    assert c.total == 29999


def test_substituicao_cupom():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("DEZ")
    c.aplicar_cupom("VINTE")
    assert c.total == 24000


def test_quantidade_zero():
    c = Carrinho()
    with pytest.raises(ValueError):
        c.adicionar(1000, 0)


def test_quantidade_negativa():
    c = Carrinho()
    with pytest.raises(ValueError):
        c.adicionar(1000, -1)


@pytest.mark.parametrize(
    "quantidade",
    [1.5, "2", None, True]
)
def test_quantidade_nao_inteira(quantidade):
    c = Carrinho()
    with pytest.raises(ValueError):
        c.adicionar(1000, quantidade)
