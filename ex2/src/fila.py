from collections import deque


class Fila:
    def __init__(self):
        self._normais = deque()
        self._prioritarias = deque()
        self._seq_normal = 0
        self._seq_prioritaria = 0

    @property
    def aguardando(self):
        return len(self._normais) + len(self._prioritarias)

    def emitir(self, tipo):
        if tipo == "prioritaria":
            self._seq_prioritaria += 1
            senha = f"P{self._seq_prioritaria}"
            self._prioritarias.append(senha)
        else:
            self._seq_normal += 1
            senha = f"N{self._seq_normal}"
            self._normais.append(senha)

        return senha

    def chamar(self):
        if self._prioritarias:
            return self._prioritarias.popleft()

        if self._normais:
            return self._normais.popleft()

        raise IndexError("fila vazia")
