def e_ano_bisexto(ano)->bool:
   return (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0 and ano % 100 == 0) or (ano % 4 != 0 and ano % 400 == 0)