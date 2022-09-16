def verifica_ano_bisexto(ano):
   
    if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0 and ano % 100 == 0) or (ano % 4 != 0 and ano % 400 == 0):
        print('Ano bissexto')
    else:
        print('Ano não é bissexto.')

        
     
     
            


