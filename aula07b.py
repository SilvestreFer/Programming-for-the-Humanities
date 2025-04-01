#A varável da função só funciona dentro da função
def count_strings(elem_list):
    index = 0
    num_strings = 0
    while index < len(elem_list):
        if type(elem_list[index]) == str:
            num_strings += 1
        index += 1
    print(f'O número de strings na lista é {index}.')
    return num_strings

number = count_strings([1, 31,'Cervantes', 'Shakespeare', 5, 'Dante'])
print(f'O número do ítens na lista é {number}.')

#Se eu executar 'print(index)' nessa posição - fora da função - a resposta no terminal é um erro "index is not defined"
