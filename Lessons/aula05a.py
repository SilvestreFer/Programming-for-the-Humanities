print('-='*11, 'Estruturas de controle', '-='*11)

title = 'Crime e castigo'
title_size = len(title)
if title_size == 15:
    print('Fiodor Dostoievsky')

rains = True
if not rains:
    print('Vou passear')
else:
    print('Leio um livro')

print('-='*11, 'Calculando idades', '-='*11)

birth_year = int(input('Digite o ano de nascimento: '))
current_year = 2025
had_birthday = str(input('Já fez aniversário? [S/N]')).strip().upper()
if had_birthday == 'S':
    print('Já fez aniversário')
    age = current_year - birth_year
else:
    print('Ainda não fez aniversário')
    age = current_year - birth_year - 1
print(f'A pessoa tem {age} anos')
