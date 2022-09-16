from src.application.input import pega_numeros
from src.application.pega_numeros import soma_numeros,multiplica_numeros,numeros_impares,numeros_pares,numeros_primos,numeros_duplicados
from src.application.output import resultado_das_operacoes

if __name__ == '__main__':
   lista_de_numeros=pega_numeros()
   soma = soma_numeros(lista_de_numeros)
   multiplicacao = multiplica_numeros(lista_de_numeros)
   lista_de_repetidos = numeros_duplicados(lista_de_numeros)
   impares = numeros_impares(lista_de_numeros) 
   pares = numeros_pares(lista_de_numeros)
   primos = numeros_primos(lista_de_numeros)
   resultado_das_operacoes(lista_de_numeros,soma,multiplicacao,lista_de_repetidos,impares,pares,primos)
