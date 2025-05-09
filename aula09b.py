import requests
response = (requests.get('https://www.fcsh.unl.pt/'))
            #A chamada request.get(que tem como parâmetro um URL) gera um objeto que colocamos na variável
print(response.status_code)
#response.json() - retorna um dicionário
