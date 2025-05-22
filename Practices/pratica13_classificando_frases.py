from time import sleep

def classificar_frase():
    frase = input(str('Digite uma frase para análise:')).strip().lower()
    if len(frase) <= 50:
        print('Curta')
    elif len(frase) > 50 and len(frase) < 100:
        print('Média')
    elif len(frase) > 100:
        print('Longa')

for c in range (3):
    classificar_frase()
    sleep(1)
