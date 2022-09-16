from src.application.input import recebe_frase
from src.application.output import frase_com_letras_maiusculas

if __name__ == '__main__':
    frase_inicial = recebe_frase()
    frase_com_letras_maiusculas(frase_inicial)
