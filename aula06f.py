#Ciclos for (com sets)

works = {'Novos ensaios sobre o entendimento humano', 'Teodiceia', 'Monadologia'}
for work in works:
    if len(work) > 15:
        continue
    else:
        print(work)
