import requests
import bs4
res=requests.get('https://www.nytimes.com/')
soup=bs4.BeautifulSoup(res.text,'lxml')
example=soup.select('.css-xdandi')
print(example)