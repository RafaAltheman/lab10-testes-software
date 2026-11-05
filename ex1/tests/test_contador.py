from contador import contar_palavras


def test_texto_vazio():
    assert contar_palavras("") == {}
