from bs4 import BeautifulSoup
import re
url = "C:\\Users\\Cody\\Documents\\Emails\\Jokers.html"
markup = open(url)
soup = BeautifulSoup(markup, "html.parser")
for script in soup(["script", "style"]): 
	script.extract()
text = soup.get_text()
text_clean = re.sub(r"\n", " ", text)
text_clean = text_clean.replace(u'\xa0', u' ')
text_clean
a = text_clean.find('From:')
text_clean[a:]
