import requests
from bs4 import BeautifulSoup

r = requests.get('https://sageelliott.com/scrape/')
soup = BeautifulSoup(r.content)
formattedContent = soup.prettify()
main_content = soup.find('div', attrs={'class': 'main-content'})

print(main_content)
