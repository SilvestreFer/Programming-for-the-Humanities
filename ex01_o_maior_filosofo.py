from time import sleep
print('Quem foi o maior filósofo? Descartes ou Kant? Vamos descobrir!!')
sleep(1)

WORK_BY_DESCARTES = int(input('Quantas obras publicou Descartes? '))
WORKS_BY_KANT = int(input('Quantas obras publicou Kant? '))
sleep(1)

if WORK_BYDESCARTES == WORKS_BY_KANT:
    print(f'Os dois filósofos publicaram o mesmo número de obras, {WORK_BYDESCARTES}. São igualmente grandiosos.')
elif WORK_BYDESCARTES > WORKS_BY_KANT:
    print('Descarte é o maior filósofo')
else:
    print('Kant é o maior filósofo')