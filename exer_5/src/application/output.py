from typing import List


def mostra_lista_de_clientes(lista_de_clientes: List[str])->None:
    print(f"Clientes {lista_de_clientes}")

def mostra_menu()->None:
    print("1- Adicionar cliente")
    print("2- Atende cliente")
    print("3- Fim")