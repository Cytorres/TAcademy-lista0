from typing import List


def pega_numeros()->List[int]:
    lista_de_numeros = []

    while True:
        numero = input('Digite números inteiros: ')
        if numero == "":
            break

        lista_de_numeros.append(int(numero))
        
    return lista_de_numeros 