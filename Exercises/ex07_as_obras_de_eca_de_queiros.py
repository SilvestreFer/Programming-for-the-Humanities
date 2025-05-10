biblio = {
    'autor': 'Eça de Queirós',
    'editora': 'Dom Quixote',
    'edição': 2025,
    'títulos': ['A Capital','O Primo Basílio', 'Os Maias']
}
print('Os obras de Eça de Queirós:')
print(biblio['autor'] + '. ' + biblio['títulos'][0] + '. ' + biblio['editora'] + ': '+ str(biblio['edição']))
print(biblio['autor'] + '. ' + biblio['títulos'][1] + '. ' + biblio['editora'] + ': '+ str(biblio['edição']))
print(biblio['autor'] + '. ' + biblio['títulos'][2] + '. ' + biblio['editora'] + ': '+ str(biblio['edição']))

#Exibição com for
print('As obras de Eça de Queirós:')
titulos = ['A Capital','O Primo Basílio', 'Os Maias']
for titulos in titulos:
    print(f'QUEIRÓS, Eça. {titulos}. Dom Quixote: 2025.')