import sys
import urllib.request
from bs4 import BeautifulSoup
print("python version:", sys.version)
url = "https://www.nytimes.com/"
res = urllib.request.urlopen(url)
webpage = res.read().decode('utf-8')
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.find('title').text)