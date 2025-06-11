
import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista
    """genera una lista de 10 numeros enteros aleatorios entre 0 y 1000.
    Retorna:
    list: Una lista de 10 numeros enteros aleatorios.
    """

def imprimir(lista):
    print("Contenido de la lista: ")   
    print(lista)    
"""Imprime la lista dada en la consola.
    Parámetros:
        lista(list): La lista a imprimir."""

def mezclar(lista):
    """Mezcla los elementos de la lista dada aleatoriamente.
    Esta funcion modifica la lista original.
    Parámetros:
        lista(list): La lista a mezclar."""
    random.shuffle(lista) 
    
# bloque principal
def main():
    """Función principal que ejecuta el programa.
    Genera una lista aleatoriamente, la imprime, la mezcla y la vuelve a imprimir.
    """
    lista = cargar()
    print("Lista generada aleatoriamente: ")
    imprimir(lista)
    mezclar(lista)
    print("La misma lista luego de mezclar: ")
    imprimir(lista)

if __name__ == "__main__":
    main()