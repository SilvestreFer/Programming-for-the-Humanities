def soma (*valores):
   s = 0
   for numero in valores:
       s += numero
   print(f'Somando os valores {valores} temos {s}.')


#Programa principal
soma(5,28)
soma(4,8,6,72)
