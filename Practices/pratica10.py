#Exercício 01 - Retornando booleanos
print(len('Kafka') == 5)
print(10>4)
print('Entrada' < 'Saída')
print('Boaventura' != 'Tomás')

#Exercício 02 - A  época histórica mais relevante
cont_articles = 15273
med_articles = 3124

if cont_articles > med_articles:
    print('A época contemporânea foi a época histórica mais relevante!')

elif cont_articles < med_articles:
    print('A época medieval foi a época histórica mais relevante!')
elif cont_articles == med_articles:
    print('Ambas as épocas são igualmente relevantes!')

#Exercício 03 - Análise de texto
text_to_analyze = 'Esta é uma frase para testar o protótipo'
quantidade_letra_a = 0
index = 0
while index < len(text_to_analyze):
    if text_to_analyze[index] == 'a':
        quantidade_letra_a += 1
        index += 1
    else:
        index += 1
print(f'A quantidade de letras "a" na frase analizada é {quantidade_letra_a}.')

#Exercício 04 - A transformação digital de uma Unidade de Investigação
#4.1
projetos_em_curso = ['cenvermos','ilegalpl','pacifico','straights']

#4.2
projeto = {
    'nome':'cenvermos',
    'número de investigadores':3,
    'investigadores':['Matias', 'Isabel', 'Ester'],
    'faculdade':'IST'
}

#4.3
index = 0

for projetos in projetos_em_curso:
    if len(projetos_em_curso[index]) >= 9:
        print(projetos_em_curso[index])
        index += 1
    else:
        index += 1

#Exercício 05 - Função do maior número

def o_maior_numero():
    lista_de_numeros = [1,5,82,28,41]
    maior_numero = 0
    index = 0
    for numero in lista_de_numeros:
        if lista_de_numeros[index] > maior_numero:
            maior_numero = lista_de_numeros[index]
            index += 1
    print(f'O maior número é {maior_numero}.')

o_maior_numero()

#Exercício 06 -

class Autor:
    def __init__(self, ano_de_nascimento, nome, obras_publicadas):
        self.ano_de_nascimento = ano_de_nascimento
        self.nome = nome
        self.obras_publicadas = obras_publicadas
    def apresentacao (self):
        print(f'Eu sou {self.nome}, nasci em {self.ano_de_nascimento} e publiquei {self.obras_publicadas}.')

primeiro_autor = Autor('1859', 'Edmund Husserl', 29)
primeiro_autor.apresentacao()