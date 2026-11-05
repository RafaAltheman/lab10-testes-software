from fila import Fila
import pytest


def test_fila_vazia():
    fila = Fila()
    assert fila.aguardando == 0
