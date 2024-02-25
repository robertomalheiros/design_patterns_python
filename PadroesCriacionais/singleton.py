class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando o objeto")
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Deve imprimir: True
