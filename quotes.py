from bs4 import BeautifulSoup
import requests

res = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(res.text,'html5lib')

quote = soup.find_all('span',{'class':'text'})

for q in quote:
    print(q.text)
    print( )






