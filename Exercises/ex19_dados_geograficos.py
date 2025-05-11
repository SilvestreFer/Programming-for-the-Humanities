import requests
def city(city_name):
    url = 'http://api.geonames.org/searchJSON?q=Amadora&maxRows=1&username=fspring'
    url_novo = url.replace('Amadora', city_name)
    resposta = requests.get(url_novo)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print('Eu encontrei um erro!')
print(city('Lisboa'))

def dados_geograficos(city_json):
