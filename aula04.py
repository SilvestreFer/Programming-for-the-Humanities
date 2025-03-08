#Igualdade:
print(2 == 1)
print('arroz' == 'massa')
print(6 == len('Camões'))

author = 'Camões'
other_author = 'Camões'
print(author == other_author)

#Diferença:
print(2 != 1)
print('arroz' != 'massa')
print(6 != len('Camões'))
print(author != other_author)

#Maior e maior igual:
print(2>=2 and 10>2)

#Menor e menor igual:
print(2<=2 and 10>2)

#and
print(len('Freud') == 5 and len('Freud') != 5)
print(abs(-3) == 4 and abs(-7) == 7)

#or
shakespeare = cervantes = 'escritores'
heidegger = hussel = 'filósofos'
print((heidegger == cervantes) or (heidegger == hussel))
print('-='*11)

#not


#Exercícios:

print('7 é igual ao número de letras do nome "Vivaldi"')
print(7 == len('Vivaldi'))
print('O valor absoluto de -7 é maior do que zero.')
print(abs(-7) > 0)
print('A palavra República vem depois de Monarquia no dicionário.')
print('República' > 'Monarquia')
print('Os conceitos de Sinfonia e Ópera são distintos.')
print('Sinfonia' != 'Ópera')
print('Guernica tem oito letras e Primavera tem 9.')
print(len('Guernica') == 8 and len('Primavera') == 9)

vasco_da_gama = colombo = 'navegador'
sagres = sevilha = 'porto'

print('sagres > sevilha')
print(sagres > sevilha)
print("colombo == 'navegador' or sevilha == 'navegador'")
print(colombo == 'navegador' or sevilha == 'navegador')
print("not(vasco_da_gama == 'navegador') and sagres == 'porto'")
print(not(vasco_da_gama == 'navegador') and sagres == 'porto')