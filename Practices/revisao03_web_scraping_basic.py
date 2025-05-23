import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
conteudo_do_link = BeautifulSoup(response.text, 'html.parser')

todos_os_links = conteudo_do_link.find_all('a')
for link in todos_os_links:
    if link.get('href') == '/':
        print(link.get_text())
