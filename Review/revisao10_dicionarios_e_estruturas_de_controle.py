def resumo_projeto():
    projeto = {
    'nome': 'CorLex',
    'pesquisadores': ['Joana', 'Rafael', 'Lia'],
    'instituicao': 'ULisboa',
    'ativo': True
    }

    print(f'O projeto tem {len(projeto['pesquisadores'])} pesquisadores.')

    if projeto['ativo'] == True:
        print('O projeto está ativo!')
    else:
        print('O projeto está inativo!')

resumo_projeto()
