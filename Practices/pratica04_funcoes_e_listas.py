#Usando listas:
def dobro(lista):
   posicao_do_elemento_da_lista = 0
   while posicao_do_elemento_da_lista < len(lista):
       lista[posicao_do_elemento_da_lista] *= 2
       posicao_do_elemento_da_lista += 1


#Programa principal:
valores = [6,3,8,15,4,13]
dobro(valores)
print(valores)
