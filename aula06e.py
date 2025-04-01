#Ciclos for (com dicionários)

democracy = {
    'poder de escolher': 'cidadão',
    'poder legislativo': 'parlamento',
    'poder executivo': 'governo',
    'poder judicial': 'tribunais'
}
print('Numa democracia:')
for power,entity in democracy.items(): #item, item e dicionário:intems()
    print('O ' + power +' pertence ao ' + entity)