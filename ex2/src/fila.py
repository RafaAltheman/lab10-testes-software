from collections import deque


class Fila:
    def __init__(self):
        self._normais = deque()
        self._prioritarias = deque()

        self._seq_normal = 0
        self._seq_prioritaria = 0
        self._prioritarias_seguidas = 0

    def emitir(self, tipo):
        if tipo == "normal":
            self._seq_normal += 1
            senha = f"N{self._seq_normal}"
            self._normais.append(senha)

        elif tipo == "prioritaria":
            self._seq_prioritaria += 1
            senha = f"P{self._seq_prioritaria}"
            self._prioritarias.append(senha)

        else:
            raise ValueError("tipo invalido")

        return senha

    @property
    def aguardando(self):
        return len(self._normais) + len(self._prioritarias)

    def chamar(self):
        if not self.aguardando:
            raise IndexError("fila vazia")

        if self._normais and (
            not self._prioritarias
            or self._prioritarias_seguidas >= 2
        ):
            self._prioritarias_seguidas = 0
            return self._normais.popleft()

        self._prioritarias_seguidas += 1
        return self._prioritarias.popleft()