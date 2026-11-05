from collections import deque


class Fila:
    def __init__(self):
        self._normais = deque()
        self._seq_normal = 0

    @property
    def aguardando(self):
        return len(self._normais)

    def emitir(self, tipo):
        self._seq_normal += 1
        senha = f"N{self._seq_normal}"
        self._normais.append(senha)
        return senha

    def chamar(self):
        if not self._normais:
            raise IndexError("fila vazia")

        return self._normais.popleft()
