#Exercício 01: Calcule o ano de falecimento de Camilo Castelo Branco

nascimento=1825
idade=65
falecimento=nascimento+idade
print(f'Camilo Castelo Branco nasceu em {nascimento} e morreu com {idade}. O seu ano de falecimento foi {falecimento}.')
print('-='*11)

#Exercício 02: Unir duas strings com o nome de Edgar Degas
nome='Edgar'
sobrenome= 'Degas'
print(f'{nome} {sobrenome}')
# -> Outra forma:
print('Edgar' +' '+ 'Degas')
print('-='*11)

#Exercício 03:
nome= 'Sebastião José de Carvalho e Melo'
print(f'A primeira letra do nome é {nome[0]}.')
print(f'A última letra do nome é {nome[-1]}.')

nobiliarquico= 'Marquês de Pombal'
print(f'O título nobiliárquico é {nobiliarquico[:7]}.')
print(f'A localidade associada ao título é {nobiliarquico[-6:]}.')

texto= 'Sebastião José de Carvalho e Melo foi Marquês de Pombal'
s=texto.split()
print(s[7])
print('-='*11)

author = 'Karl Marx'
work = 'O Capital'
print('O autor', author, 'escreveu', work)
print('-='*11)

language='Python'
print(language)
print('-='*11)

number_of_pages = 146
print(type(number_of_pages))
print('-='*11)

