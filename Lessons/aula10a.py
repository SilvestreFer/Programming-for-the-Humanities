import requests
from bs4 import BeautifulSoup


url = 'https://www.ucl.ac.uk/lbs/inventories/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
soup = soup.find('table')

for row in soup.find_all('tr'):
    dat = row.find('div', attrs={'class': 'six columns small'})
    name = dat.a.get_text()
    link = 'https://www.ucl.ac.uk' + dat.a.get('href')
    print(f'{name} - {link}')

url = 'https://portal.cehr.ft.lisboa.ucp.pt/BeliefAndCitizenship/BDImprensa/DisplayAdvancedSearchResults.php?viewPage=0&ordenationCriteria=name'
response = requests.get(url)
