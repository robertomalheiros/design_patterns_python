num = 0
str = "Hola Mundo"
list = [1, 2, 3, 4, 5]
dict = {"nombre": "Juan", "apellido": "Perez"}
tupl = (1, 2, 3, 4, 5)
bool = True
float = 1.5
none = None

#criando uma função de leitura de dicionários
def read_dict(dict):
    for key, value in dict.items():
        return f"{key}: {value}"

# imprimindo todos os valores das variáveis de uma vez só

print(f"Numero: {num} \nString: {str} \nLista: {list} \nDicionario: {read_dict(dict)} \nTupla: {tupl} \nBooleano: {bool} \nFlutuante: {float} \nNada: {none}")

dir(str)