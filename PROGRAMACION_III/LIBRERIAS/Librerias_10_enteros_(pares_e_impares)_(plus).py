import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,100))
    return lista


def imprimir(lista):
    print(lista)    

def separar(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
            print("Números impares: ", impares)
            print("Números pares: ", pares)
    
# bloque principal

lista=cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
separar(lista)
print("Números de la lista separados por pares e impares")
imprimir(lista)