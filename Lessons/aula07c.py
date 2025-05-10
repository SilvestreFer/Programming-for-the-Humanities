#Substituição na função

def change_first(elem_list, first):
    elem_list[0] = first

name_list = ['Boticelli', 'Van Gogh', 'Velazquez']
change_first(name_list, 'Michelangelo')
print(f'A nova lista é {name_list}')

#Aqui eu usei uma função para executar a troca
