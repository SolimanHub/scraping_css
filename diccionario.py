import requests
from bs4 import BeautifulSoup as b

url='https://www.mclibre.org/consultar/htmlcss/css/css-propiedades.html'
html=requests.get(url)

content=html.content
soup=b(content,"html.parser")

tabla=soup.find("table")
td=tabla.find_all('td')
 
for i in td:
    print(i.text)
