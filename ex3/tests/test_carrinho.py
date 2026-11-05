import pytest
from carrinho import Carrinho


def test_vazio():
    assert Carrinho().total == 0


def test_preco_unico():
    c = Carrinho()
    c.adicionar(2500)

    assert c.total == 2500


def test_quantidade_dois():
    c = Carrinho()
    c.adicionar(2500, 2)

    assert c.total == 5000


def test_preco_zero_rejeitado():
    c = Carrinho()

    with pytest.raises(ValueError):
        c.adicionar(0)


def test_cupom_invalido():
    c = Carrinho()

    with pytest.raises(ValueError):
        c.aplicar_cupom("XYZ")


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


def test_dez_antes_minimo():
    c = Carrinho()
    c.adicionar(9999)
    c.aplicar_cupom("DEZ")

    assert c.total == 9999


def test_dez_apos_adicao():
    c = Carrinho()
    c.adicionar(9000)
    c.aplicar_cupom("DEZ")
    c.adicionar(1000)

    assert c.total == 9000


def test_vinte_abaixo_minimo():
    c = Carrinho()
    c.adicionar(29999)
    c.aplicar_cupom("VINTE")

    assert c.total == 29999


def test_vinte_no_minimo():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("VINTE")

    assert c.total == 24000


def test_substituicao_cupom():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("DEZ")
    c.aplicar_cupom("VINTE")

    assert c.total == 24000


def test_substituicao_por_cupom_inelegivel():
    c = Carrinho()
    c.adicionar(10000)
    c.aplicar_cupom("DEZ")
    c.aplicar_cupom("VINTE")

    assert c.total == 10000


@pytest.mark.parametrize(
    "quantidade",
    [0, -1, 1.5, "2", None, True]
)
def test_quantidade_invalida(quantidade):
    c = Carrinho()

    with pytest.raises(ValueError):
        c.adicionar(1000, quantidade)


def test_quantidade_valida():
    c = Carrinho()
    c.adicionar(1000, 1)
    c.adicionar(1000, 3)

    assert c.total == 4000