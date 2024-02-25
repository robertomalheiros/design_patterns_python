class Observador:
    def atualizar(self, mensagem):
        pass

class ObservadorConcreto(Observador):
    def atualizar(self, mensagem):
        print(f"ObservadorConcreto: {mensagem}")

class Sujeito:
    def __init__(self):
        self._observadores = []

    def registrar(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensagem):
        for observador in self._observadores:
            observador.atualizar(mensagem)

sujeito = Sujeito()
observador = ObservadorConcreto()
sujeito.registrar(observador)
sujeito.notificar("Olá!")  # Deve imprimir: "ObservadorConcreto: Olá!"
