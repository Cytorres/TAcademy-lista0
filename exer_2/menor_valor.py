def pega_inteiro(message:str, error_message:str, lowest:int, highest:int)->int:

    while True:
        user_input = input(message)

        if not (user_input.isdigit()):
            print (error_message, user_input)
            continue

        user_input_converted = int(user_input)
        if (lowest != None) and (user_input_converted < lowest):
            print (error_message, user_input)
            continue

        if (highest != None) and (user_input_converted > highest):
            print (error_message, user_input)
            continue

        return user_input_converted
    
    
numero_execucoes = pega_inteiro("Informe quantas questoes?", "Tem que ser maior que zero", 1, None)