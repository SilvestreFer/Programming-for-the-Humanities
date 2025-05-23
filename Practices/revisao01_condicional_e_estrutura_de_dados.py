palavra = input('Digite uma palavra pra análise: ')
if len(palavra) > 5:
    print('Palavra longa')
elif len(palavra) > 3:
    print('Palavra média')
else:
    print('Palavra curta')
