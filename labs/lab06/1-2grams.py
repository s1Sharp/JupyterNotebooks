from urllib.request import urlopen
from bs4 import BeautifulSoup

def getNgrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))

# def ngraMs(input, n):
#     content= re.sub('\n+', " " , content)
#     content= re.sub(' +', " " , content)
#     content = bytes(content, "UTF-8" )
#     content= content.decode( "ascii" , "ignore")
#     print(content)
#     input = input.split(' ') 
#     output = []
#     for i i.n range(len(input)-n+l):
#      output.append(input[i:i+n])
#     return output