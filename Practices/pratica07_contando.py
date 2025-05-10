from time import sleep

def contador(inicio, fim, passo):
   if passo == 0:
       passo = 1

   if inicio > fim and passo > 0:
       passo = -passo
   elif inicio < fim and passo < 0:
       passo = -passo

   print('-=' * 30)
   print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

   for numero in range (inicio, fim, passo):
       print(numero, end=' ')
       sleep(1)
       numero += 1
   print('FIM!')

#Programa principal
contador(1,10,1)

contador(10,0,-2)

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(inicio = int(input('Início: ')),
   fim = int(input('Fim: ')),
   passo = int(input('Passo: ')))
