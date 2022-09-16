from src.application.input import pega_opcao,recebe_nome_cliente
from src.application.output import mostra_menu,chama_cliente

if __name__== '__main__':
    pilha_de_clientes = []
    while True:
        mostra_menu()
        codigo = pega_opcao()

        if not codigo in (1,2,3):
            print('ERRO...Digite um código valido')
            continue

        if codigo == 1:
            nome = recebe_nome_cliente()
            pilha_de_clientes.append(nome)

        elif codigo == 2:
            if len(pilha_de_clientes) == 0:
                print("Não há cliente para ser atendido")
            else:
               nome: str =  pilha_de_clientes.pop(-1)
               chama_cliente(nome)
        else:
            print("FIM")
            break
            

        
