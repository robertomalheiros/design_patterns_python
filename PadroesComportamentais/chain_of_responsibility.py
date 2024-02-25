class Manipulador:
    def __init__(self):
        self._proximo = None

    def set_proximo(self, manipulador):
        self._proximo = manipulador
        return manipulador

    def manipular(self, requisicao):
        if self._proximo:
            return self._proximo.manipular(requisicao)

class ManipuladorConcreto1(Manipulador):
    def manipular(self, requisicao):
        if requisicao == 1:
            return "Um"
        else:
            return super().manipular(requisicao)

class ManipuladorConcreto2(Manipulador):
    def manipular(self, requisicao):
        if requisicao == 2:
            return "Dois"
        else:
            return super().manipular(requisicao)

manipulador = ManipuladorConcreto1()
manipulador.set_proximo(ManipuladorConcreto2())

print(manipulador.manipular(1))  # Deve imprimir: "Um"
print(manipulador.manipular(2))  # Deve imprimir: "Dois"
print(manipulador.manipular(3))  # Deve imprimir: None
