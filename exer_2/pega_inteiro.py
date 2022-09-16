def pega_inteiro(mensagem:str, mensagem_erro:str, menor_valor:int, maior_valor:int)->int:
     while True:
        entrada_usuario = input(mensagem)
        if not (entrada_usuario.isdigit()):
            print(mensagem_erro)
            continue

        entrada_usuario_inteiro = int(entrada_usuario)
        if (menor_valor != None) and (entrada_usuario_inteiro < menor_valor):
            print(mensagem_erro)
            continue

        if (maior_valor != None) and (entrada_usuario_inteiro > maior_valor):
            print(mensagem_erro)
            continue
        return entrada_usuario_inteiro

mensagem = pega_inteiro("Informe o valor: ","Tem que estar entre 0 e 99", 0, 99)