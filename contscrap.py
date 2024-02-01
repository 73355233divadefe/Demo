import requests

from bs4 import BeautifulSoup

url = 'https://arielahomecare.co.uk'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting information from the webpage
    title = soup.title.text
    paragraphs = soup.find_all('p')

    print(f'Title: {title}')
    print('paragraphs:')
    for i, paragraph in enumerate(paragraphs, 1):
        print(f'{i}. {paragraph.text}')
else:
    print(f'Error: {response.status_code}')