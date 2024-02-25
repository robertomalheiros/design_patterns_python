class Singleton:
    _instancia = None
    _constante = None

    def __new__(cls, constante=None):
        if cls._instancia is None:
            print("Criando o objeto")
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia

    def __init__(self, constante=None):
        if self._constante is None:
            self._constante = constante

