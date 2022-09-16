from typing import List
import math


def soma_numeros(lista_de_numeros: List[int]):
    return sum(lista_de_numeros)

def multiplica_numeros(lista_de_numeros: List[int]):
    return math.prod(lista_de_numeros)

def numeros_duplicados(lista_de_numeros:List[int]):
    lista_de_repetidos = []
    nao_repetidos = [set(lista_de_numeros)]
    for numero in lista_de_numeros:
        if numero in nao_repetidos == 2:
            lista_de_repetidos.append(numero)

    return lista_de_repetidos

def numeros_impares(lista_de_numeros: List[int])->List[int]:
    numeros_impares = []
    for numero in lista_de_numeros:
        if numero % 2 != 0:
            numeros_impares.append(numero)
    return numeros_impares

def numeros_pares(lista_de_numeros: List[int])->List[int]:
    numeros_pares = []
    for numero in lista_de_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

def isPrime(n):
        start = 2

        while start <= math.sqrt(n):
            if n % start < 1:
                return n
            start += 1

        return n > 1
def numeros_primos(lista_de_numeros:List[int])->List[int]:
    numeros_primos = []
    for numero in lista_de_numeros:
        if isPrime(numero) == True:
         numeros_primos.append(numero)
        
    return numeros_primos
        



        