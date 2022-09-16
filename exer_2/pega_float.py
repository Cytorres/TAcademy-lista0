


def pega_float(mensagem:str, mensagem_erro:str, menor_valor:float, maior_valor:float)->float:
     while True:
        try:
            entrada_usuario = input(mensagem)
            entrada_usuario_float = float(entrada_usuario)
        except:
            print(mensagem_erro)
            continue

        if (menor_valor != None) and (entrada_usuario_float < menor_valor):
            print(mensagem_erro)
            continue

        if (maior_valor != None) and (entrada_usuario_float > maior_valor):
            print(mensagem_erro)
            continue
        return entrada_usuario_float

mensagem = pega_float("Informe o valor: ","Tem que estar entre 0.0 e 99.99", 0.0, 99.99)