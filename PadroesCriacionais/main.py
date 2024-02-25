# main.py

import os
import sys

# Obtenha o caminho absoluto do diretório que contém o script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Adicione o diretório ao sys.path
sys.path.append(diretorio_atual)

# Agora você pode importar o módulo
from singleton_constante import Singleton

# O resto do seu código vai aqui
s1 = Singleton("valor inicial")
s2 = Singleton()

print(s1 is s2)  # Deve imprimir: True
print(s1._constante)  # Deve imprimir: "valor inicial"
print(s2._constante)  # Deve imprimir: "valor inicial"