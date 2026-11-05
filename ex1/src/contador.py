def contar_palavras(texto):
    contagem = {}

    for palavra in texto.split():
        palavra = palavra.lower().strip(".,;:!?")

        if not palavra:
            continue

        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem