#Contando as letras de um título:

titulo_da_obra = str(input('Digite o nome da obra: ')).strip()

titulo_da_obra_sem_espacos = titulo_da_obra.split()
tamanho_do_titulo = len("".join(titulo_da_obra_sem_espacos))

print(f'O título da obra "{titulo_da_obra}" tem {tamanho_do_titulo} caracteres.')

#Outra forma:

titulo_da_obra = str(input('Digite o nome da obra: ')).strip()

titulo_da_obra_sem_espacos = titulo_da_obra.replace(" ", "")
tamanho_do_titulo = len(titulo_da_obra_sem_espacos)

print(f'O título da obra "{titulo_da_obra}" tem {tamanho_do_titulo} caracteres.')