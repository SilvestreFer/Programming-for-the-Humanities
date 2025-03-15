INITIAL = 'Oh Fortuna velut luna statu variabilis'
current_index = 0

while current_index < len(INITIAL):
    if INITIAL[current_index] == 'u': #precisa ser igual para encontrar o 'u'
        current_index += 1
        continue #vai pular o 'u'
    print(INITIAL[current_index], end='') #o print só vem aqui para mostrar toda a frase sem o 'u'
    current_index += 1
print()

#Outra forma
INITIAL = 'Oh Fortuna velut luna statu variabilis'
current_index = 0
sem_u = ''
while current_index < len(INITIAL):
    if INITIAL[current_index] == 'u':
        current_index += 1
        continue
    sem_u += INITIAL[current_index] #concatenização da string
    current_index += 1
print(sem_u)