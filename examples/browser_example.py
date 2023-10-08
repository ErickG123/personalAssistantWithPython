import requests
import webbrowser as browser
from bs4 import BeautifulSoup

url = f'https://youtube.com/results?search_query=beliver'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find_all('a'))

# links = soup.find_all(id='video-title')

# print(links)
