def listar_autoras_por_nacionalidade():
    autoras = [
        {'nome': 'Clarisse Lispector', 'nacionalidade':'brasileira'},
        {'nome': 'Virginia Woolf', 'nacionalidade':'britânica'},
        {'nome': 'Carolina Maria de Jesus', 'nacionalidade': 'brasileira'},
        {'nome': 'Simone de Beauvoir', 'nacionalidade': 'francesa'}
    ]
    for autora in autoras:
        if autora['nacionalidade'] == 'brasileira':
            print(autora['nome'])

listar_autoras_por_nacionalidade()