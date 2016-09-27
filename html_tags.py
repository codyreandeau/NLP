'''
This finds all of the html tags
in Googles homepage

'''

import nltk
from bs4 import BeautifulSoup
from urllib import request
url='https://www.google.com'
html=request.urlopen(url).read()
raw=html.decode('latin-1')
soup = BeautifulSoup(html, "html.parser")
[tag.name for tag in soup.find_all()]