def menor_numero(lista):
    o_menor = lista[0]
    for numero in lista:
        if numero < o_menor:
            o_menor = lista[numero]
        elif numero > o_menor:
            o_menor = o_menor
    print(f'O menor número da lista é {o_menor}.')

menor_numero([2,85,64,75,21,4,99])
