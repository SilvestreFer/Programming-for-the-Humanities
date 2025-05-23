def contar_vogais(frase):
    a=e=i=o=u=0
    print('Analisando a frase...')
    print('Aqui está as vogais que eu contei: ')
    for letra in frase:
        if letra == 'a':
            a += 1
        elif letra == 'e':
            e += 1
        elif letra == 'i':
            i += 1
        elif letra == 'o':
            o += 1
        elif letra == 'u':
            u += 1

    print(f'A = {a}; E = {e}; I = {i}; O = {o}; U = {u}')

contar_vogais('A investigação científica é importante.')
