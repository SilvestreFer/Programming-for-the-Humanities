import requests
from bs4 import BeautifulSoup
from time import sleep

url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'

def coletar_titulos_em_destaque():
    response = requests.get(url)
    conteudo_do_link = BeautifulSoup(response.text, 'html.parser')

    titulos = conteudo_do_link.find_all('a')

    for titulo in titulos:
        href = titulo.get('href','')
        if href.startswith('/wiki/') and ':' not in href:
            titulo_do_artigo = titulo.get_text()
            print(titulo_do_artigo)
            sleep(1)

coletar_titulos_em_destaque()
