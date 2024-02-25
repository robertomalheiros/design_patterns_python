from abc import ABC, abstractmethod

class Estrategia(ABC):
    @abstractmethod
    def executar(self, a, b):
        pass

class Adicao(Estrategia):
    def executar(self, a, b):
        return a + b

class Subtracao(Estrategia):
    def executar(self, a, b):
        return a - b

class Contexto:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def executar_estrategia(self, a, b):
        return self._estrategia.executar(a, b)

contexto = Contexto(Adicao())
print(contexto.executar_estrategia(3, 4))  # Deve imprimir: 7

contexto = Contexto(Subtracao())
print(contexto.executar_estrategia(3, 4))  # Deve imprimir: -1
