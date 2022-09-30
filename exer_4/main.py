from src.application.input import pega_data
from src.application.verifica_ano_bsisexto import e_ano_bisexto
from src.application.output import mostra_mensagem

if __name__ == '__main__':
    ano = pega_data()
    if e_ano_bisexto(ano):
        mostra_mensagem("E bissexto")
    else:
        mostra_mensagem("Nao é bissexto")