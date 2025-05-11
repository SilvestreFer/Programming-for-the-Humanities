import requests
def chamada():
    resposta = requests.get('http://api.geonames.org/searchJSON?q=Amadora&maxRows=1&username=fspring')
    if resposta.status_code == 200:
        print(resposta.json())
    else:
        print('Eu encontrei um erro!')
chamada()
