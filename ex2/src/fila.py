class Fila:
    def __init__(self):
        self.aguardando = 0

    def chamar(self):
        raise IndexError("fila vazia")
