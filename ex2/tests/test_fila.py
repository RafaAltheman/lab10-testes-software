import pytest
from fila import Fila


def test_vazia():
    f = Fila()

    assert f.aguardando == 0

    with pytest.raises(IndexError):
        f.chamar()


def test_normal():
    f = Fila()

    assert f.emitir("normal") == "N1"
    assert f.emitir("normal") == "N2"

    assert f.aguardando == 2
    assert f.chamar() == "N1"
    assert f.chamar() == "N2"


def test_prioritaria():
    f = Fila()

    assert f.emitir("prioritaria") == "P1"
    assert f.emitir("prioritaria") == "P2"

    assert f.chamar() == "P1"
    assert f.chamar() == "P2"


def test_tipo_invalido():
    f = Fila()

    with pytest.raises(ValueError):
        f.emitir("urgente")


def test_independencia_numeracao():
    f = Fila()

    assert [
        f.emitir(t)
        for t in (
            "normal",
            "prioritaria",
            "normal",
            "prioritaria"
        )
    ] == ["N1", "P1", "N2", "P2"]


def test_prioridade():
    f = Fila()

    f.emitir("normal")
    f.emitir("prioritaria")

    assert f.chamar() == "P1"
    assert f.chamar() == "N1"


def test_limite_duas_prioritarias():
    f = Fila()

    f.emitir("normal")

    for _ in range(3):
        f.emitir("prioritaria")

    assert [f.chamar() for _ in range(4)] == [
        "P1", "P2", "N1", "P3"
    ]


def test_zerar_contagem():
    f = Fila()

    for tipo in (
        "normal",
        "normal",
        "prioritaria",
        "prioritaria",
        "prioritaria",
        "prioritaria"
    ):
        f.emitir(tipo)

    assert [f.chamar() for _ in range(6)] == [
        "P1", "P2", "N1", "P3", "P4", "N2"
    ]


def test_sem_normal_nao_limita():
    f = Fila()

    for _ in range(4):
        f.emitir("prioritaria")

    assert [f.chamar() for _ in range(4)] == [
        "P1", "P2", "P3", "P4"
    ]


def test_normal_chega_depois_duas_prioritarias():
    f = Fila()

    for _ in range(3):
        f.emitir("prioritaria")

    f.chamar()
    f.chamar()
    f.emitir("normal")

    assert f.chamar() == "N1"


def test_quantidade_diminui():
    f = Fila()

    f.emitir("normal")
    assert f.aguardando == 1

    f.chamar()
    assert f.aguardando == 0