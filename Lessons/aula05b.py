print('-='*11, 'Ciclos', '-='*11)

while_limit = 5
current_index = 0
while current_index < while_limit:
    print(current_index)
    current_index += 1

name = 'Verdi'
current_index = 0
while current_index < len(name):
    print(name[current_index]) #os [] retomam a posição das letras
    current_index += 1

name = 'Verdi'
current_index = 0
while current_index < len(name):
    if name[current_index] == 'd':
        break #função para parar o loop
    print(name[current_index], end='')
    current_index += 1
print()
print(f'O ciclo parou no index {current_index}')
print(f'A palavra tem um tamanho de {len(name)} caracteres')

name = 'Verdi'
current_index = 0
while current_index < len(name):
    if name[current_index] == 'r':
        current_index += 1
        continue
    print(name[current_index], end='')
    current_index += 1
print()
print(current_index)

name = 'Verdi'
current_index = 0
while current_index < len(name):
    if name[current_index] == 'r':
        continue #esse criou um infinito, ele so executa a linha 40 e 41 e o 'continue' faz ele continuar executando.
    print(name[current_index])
    current_index += 1
print()
print(current_index)