import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_internal_links(url):
    internal_links = set()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href.startswith('/') or href.startswith(url):
            internal_links.add(urljoin(url, href))
    
    return internal_links

def parse(url):
   
   internal_links = get_internal_links(url)

   for link in internal_links:
      print(link)
      requests.get(link)


url = input('Введи ссылку (https://example.com/) >> ')

print('start parsing...')
parse(url)