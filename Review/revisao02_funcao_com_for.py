def conta_impares(lista):
    quantidade_de_inteiros = 0
    for numero in lista:
        if numero%2 != 0:
            quantidade_de_inteiros += 1
    print(f'A sua lista tem {quantidade_de_inteiros} números inteiros.')

conta_impares([7,28,4500,13,27])
