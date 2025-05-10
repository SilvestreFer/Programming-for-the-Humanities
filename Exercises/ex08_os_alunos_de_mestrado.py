#Mostrando os alunos matriculados

ADEH = {2021130375, 2021133276, 2021109373, 2020125614} #Análise de Dados Espaciais nas Humanidades
IPH = {2024102970, 2021132908, 2021133276, 2024130299, 2021130375} #Introdução à Programação nas Humanidades
print(f'Os alunos inscritos nas cadeiras de ADEH e IPH são {ADEH|IPH}')
print(f'Os alunos cursando as duas cadeiras são {ADEH&IPH}')
