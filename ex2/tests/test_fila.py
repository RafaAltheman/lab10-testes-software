from fila import Fila
import pytest


def test_fila_vazia():
    fila = Fila()
    assert fila.aguardando == 0


def test_chamar_fila_vazia():
    fila = Fila()

    with pytest.raises(IndexError):
        fila.chamar()
