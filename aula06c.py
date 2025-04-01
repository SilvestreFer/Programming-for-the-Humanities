#Estrutura de dados - SETS {,}

students = {53891, 39170, 7829}
print(students) #tem ordem aleatória
students = {53891, 39170, 7829, 39170, 892, 892}
print(len(students)) #conta os números desconsiderando os repetidos como ítem da contagem
print(students) #não mostra o que é repetido
print()
philosophers = {'Plotino', 'Tomás de Aquino', 'Descartes', 'Hume', 'Agostinho'}
theologians = {'Tomás de Aquino', 'Agostinho', 'Karl Rahner'}
print(f'Foram filósofos e/ou teólogos: {philosophers|theologians}') #o | é usado para juntar os dois sets, mas não repete o que é igual
print(f'Foram filósofos e teólogos: {philosophers & theologians}') #o & mostra o que é comum nas duas sets