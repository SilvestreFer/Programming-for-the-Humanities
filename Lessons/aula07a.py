#Funções

def mystery_function(arg1, arg2, arg3):
    if arg3 : #retorna um boleano
        new_object = [arg1, arg2] #retona uma lista
    else:
        new_object = {arg1:arg2} #retorna sets
    return new_object
result = mystery_function('Nome', 'Mozart', False)
print(result)

def alt_myst_function(data_struc):
    i = 0
    for elem in data_struc:
        i += elem
    return i
result = alt_myst_function([3,6,7,4])
print(f'A soma dos ítens da lista é {result}.')

def alt_myst_function(data_struc):
    i = ''
    for elem in data_struc:
        i += elem
    return i
result = alt_myst_function(['Eu ', 'consigo ', 'aprender ', 'isso!'])
print(result)
