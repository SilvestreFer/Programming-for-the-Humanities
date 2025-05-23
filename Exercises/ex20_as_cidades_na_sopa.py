import requests # ver https://requests.readthedocs.io/en/latest/
from bs4 import BeautifulSoup # ver https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import time # ver https://docs.python.org/3/library/time.html#time.sleep
import re # ver https://www.w3schools.com/python/python_regex.asp

url = "https://portal.cehr.ft.lisboa.ucp.pt/BeliefAndCitizenship/BDImprensa/DisplayAdvancedSearchResults.php?viewPage=0&ordenationCriteria=name"

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

text = html.find('h4').getText()
numero = re.findall(r"\d+", text)
numero_de_paginas = int(numero[0]) / 20 + 1

pagina = 0
while pagina < numero_de_paginas:
    url = "https://portal.cehr.ft.lisboa.ucp.pt/BeliefAndCitizenship/BDImprensa/DisplayAdvancedSearchResults.php?viewPage=" + str(pagina) + "&ordenationCriteria=name"
    url_base = "https://portal.cehr.ft.lisboa.ucp.pt/BeliefAndCitizenship/BDImprensa/"
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')

    links = html.find_all('a')
    for link in links:
        if link.get_text() == "Ver Mais":
            link_a_abrir = url_base + link.attrs['href']
            abrir_link = requests.get(link_a_abrir)
            html = BeautifulSoup(abrir_link.text, 'html.parser')

            titulos = html.find_all("td", style="width:710px; font-size:150%; line-height:1;word-wrap:break-word; vertical-align:middle;")
            for titulo in titulos:
                nome_jornal = titulo.getText()

            linhas = html.find_all("td")
            for linha in linhas:
                texto_da_linha = linha.getText()
                if texto_da_linha.find("Local de Edição: ") > -1:
                    localidade = texto_da_linha.replace("Local de Edição: ", "")
                if texto_da_linha.find("Data de Início: ") > -1:
                    data = texto_da_linha.replace("Data de Início: ", "")

            print(nome_jornal + "; " + localidade + "; " + str(data))

            time.sleep(1)

    pagina += 1