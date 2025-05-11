import requests
from bs4 import BeautifulSoup

url = 'https://portal.cehr.ft.lisboa.ucp.pt/BeliefAndCitizenship/BDImprensa/DisplayAdvancedSearchResults.php?viewPage=0&ordenationCriteria=name'
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')
print(html)
