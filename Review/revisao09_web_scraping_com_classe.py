import requests
from bs4 import BeautifulSoup
from time import sleep

class SiteDeFrases():
    def __init__(self, url_base):
        self.url_base = url_base
        self.conteudo_html = None

    def extrair_frases(self):
        response = requests.get(self.url_base)
        self.conteudo_html = BeautifulSoup(response.text,'html.parser')

        todas_as_frases = self.conteudo_html.find_all(class_="text")
        for frase in todas_as_frases:
            print(frase.get_text())
        sleep (1)

site = SiteDeFrases('https://quotes.toscrape.com/')
site.extrair_frases()
