from typing import List
from src.application.input import pega_opcao_cliente, pega_nome_cliente
from src.application.output import mostra_lista_de_clientes, mostra_menu
if __name__ == '__main__':
    #codigo,cliente_novo = menu_cliente()
    #lista_de_clientes = pega_cliente(codigo,cliente_novo)
    #mostra_lista_de_clientes(lista_de_clientes)
    lista_de_clientes:List[str] = []
    while True:
        mostra_menu()
        codigo = pega_opcao_cliente()

        if not codigo in (1,2,3):
            print('Erro... Digite o código certo.')
            continue
                
        if codigo == 1:
            nome = pega_nome_cliente()
            lista_de_clientes.append(nome)
        elif codigo == 2:
            if (len(lista_de_clientes) == 0):
                print("Não ha cliente a ser atendido")
            else:
                nome: str = lista_de_clientes.pop(0)
                print(f"Cliente a ser atendido: {nome}")
        else:    
            print('FIM')
            break

    mostra_lista_de_clientes(lista_de_clientes)



