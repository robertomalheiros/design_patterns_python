class IteradorConcreto:
    def __init__(self, dados):
        self._dados = dados
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < len(self._dados):
            resultado = self._dados[self._indice]
            self._indice += 1
            return resultado
        raise StopIteration

dados = [1, 2, 3, 4, 5]
iterador = IteradorConcreto(dados)

for dado in iterador:
    print(dado)  # Deve imprimir: 1, 2, 3, 4, 5
