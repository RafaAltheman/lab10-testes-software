from fila import Fila
import pytest


def test_fila_vazia():
    fila = Fila()
    assert fila.aguardando == 0


def test_chamar_fila_vazia():
    fila = Fila()

    with pytest.raises(IndexError):
        fila.chamar()


def test_senhas_normais():
    fila = Fila()

    assert fila.emitir("normal") == "N1"
    assert fila.emitir("normal") == "N2"
    assert fila.aguardando == 2
    assert fila.chamar() == "N1"
    assert fila.chamar() == "N2"


def test_senhas_prioritarias():
    fila = Fila()

    assert fila.emitir("prioritaria") == "P1"
    assert fila.emitir("prioritaria") == "P2"
    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"


def test_tipo_invalido():
    fila = Fila()

    with pytest.raises(ValueError):
        fila.emitir("urgente")
