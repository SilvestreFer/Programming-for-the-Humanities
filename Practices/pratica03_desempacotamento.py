#Desempacotamento
def contador(*numero):
   #O asterisco serve para dizer que não sei quantos parâmetros vão vir
   tamanho = len(numero)
   print(f'Recebi os valores {numero} e são ao todo {tamanho}.')

#Programa principal
contador(2,5,8)
contador(8,0)
contador(4,4,8,6,2) #Gera uma tupla
