import requests
from bs4 import BeautifulSoup

url = "http://arielahomecare.co.uk"
response = requests.get(url)

if response.status_code == 200:
    Soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.text
    print(f'Titleof the page: {title}')

    links = soup.find_all('a')
    print('\nlinks on the page:')
    for link in links:
        href =link.get('href')
        if  href:
        print(link.get('href'))
else:
        print(f'Error: Unable to fetch the page. status code: {response.status_code}')
