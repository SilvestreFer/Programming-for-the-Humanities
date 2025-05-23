import requests
from bs4 import BeautifulSoup
from time import sleep

class Citações():
    def __init__(self,url):
        self.url = url

    def extrair_autores(self):
        response = requests.get(self.url)
        conteudo = BeautifulSoup(response.text,'html.parser')
        autores = conteudo.find_all('small', class_='author')
        for autor in autores:
            print(autor.get_text())
        sleep(1)

site = Citações('https://quotes.toscrape.com/')
site.extrair_autores()
