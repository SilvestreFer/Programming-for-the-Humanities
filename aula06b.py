#Estrutura de dados - DICIONÁRIOS {,}

work = {
    'author':'Immanuel Kant',
    'title': 'Kritik der reinen Verni«unft',
    'year': 1781,
    'editions': [1,2,3,4,5,6]
}
print(work['author'])
print(work['title'])
print(work['editions'])

#Alterando elementos de um dicionário
work['editions'] = [1,2,3,4,5,6,7,8,9] #novo valor para a chave 'editions'
print(work)

#Contando o tamanho de um dicionário
print(len(work)) #conta o número de chave-valor do dicionário