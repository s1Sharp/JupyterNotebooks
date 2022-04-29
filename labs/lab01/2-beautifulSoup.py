from urllib.request import urlopen
from bs4 import BeautifulSoup

#html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
html = urlopen("https://kpfu.ru/computing-technology/about")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)
print(bsObj.get_text()) 
