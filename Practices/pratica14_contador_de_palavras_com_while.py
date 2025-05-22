while True:
    frase = input(str('Digite uma frase para análise: ')).strip().lower()
    if frase == 'sair':
        print('Programa encerrado!')
        break
    else:
        lista_de_palavras_da_frase = frase.split()
        numero_de_palavras = len(lista_de_palavras_da_frase)
        print(f'A frase tem {numero_de_palavras} palavras.')
