from contador import contar_palavras


def test_texto_vazio():
    assert contar_palavras("") == {}


def test_uma_palavra():
    assert contar_palavras("teste") == {"teste": 1}


def test_duas_palavras():
    assert contar_palavras("bom dia") == {
        "bom": 1,
        "dia": 1
    }


def test_palavra_repetida():
    assert contar_palavras("dia a dia") == {
        "dia": 2,
        "a": 1
    }


def test_maiusculas_minusculas():
    assert contar_palavras("Dia dia DIA") == {
        "dia": 3
    }


def test_espacos_multiplos():
    assert contar_palavras("bom   dia") == {
        "bom": 1,
        "dia": 1
    }


def test_quebra_linha():
    assert contar_palavras("bom\ndia") == {
        "bom": 1,
        "dia": 1
    }


def test_hifen():
    assert contar_palavras("guarda-chuva") == {
        "guarda-chuva": 1
    }


def test_ponto_exclamacao():
    assert contar_palavras("fim. Fim!") == {
        "fim": 2
    }


def test_virgula_ponto_virgula():
    assert contar_palavras(",dia, ;dia;") == {
        "dia": 2
    }


def test_dois_pontos_interrogacao():
    assert contar_palavras(":dia: ?dia?") == {
        "dia": 2
    }


def test_somente_pontuacao():
    assert contar_palavras("... !") == {}