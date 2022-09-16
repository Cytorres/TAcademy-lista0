from src.application.input import pega_data
from src.application.verifica_ano_bsisexto import verifica_ano_bisexto

if __name__ == '__main__':
    ano = pega_data()
    verifica_ano_bisexto(ano)