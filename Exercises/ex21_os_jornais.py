import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://portal.cehr.ft.lisboa.ucp.pt/BeliefAndCitizenship/BDImprensa/DisplayAdvancedSearchResults.php?viewPage=0&ordenationCriteria=name"
resposta = requests.get(url)
html = BeautifulSoup(resposta.text, 'html.parser')
url_base = "https://portal.cehr.ft.lisboa.ucp.pt/BeliefAndCitizenship/BDImprensa/"

links = html.find_all('a')
for link in links:
    if link.get_text() == 'Ver Mais':
        abrindo_o_link = url_base + link.attrs['href']
        abrir_link = requests.get(abrindo_o_link)
        html_cada_link = BeautifulSoup(abrir_link.text, 'html.parser')

        titulos = html_cada_link.find_all("td",style="width:710px; font-size:150%; line-height:1;word-wrap:break-word; vertical-align:middle;")
        for titulo in titulos:
            titulo_do_jornal_lido = titulo.get_text()
            print(titulo_do_jornal_lido)

        locais_de_edicao = html_cada_link.find_all("td", style="width: 400px; word-wrap:break-word; vertical-align:top;")
        for local in locais_de_edicao:
            nome_do_local = local.get_text()
            if nome_do_local.find("Local de Edição") >= 0:
                print(nome_do_local)

        datas_de_inicio = html_cada_link.find_all("td", style="width: 400px; word-wrap:break-word; vertical-align:top;")
        for data in datas_de_inicio:
            data_local = data.get_text()
            if data_local.find("Data de Início") >= 0:
                print(data_local)
        print('-='*30)
        sleep(1)
