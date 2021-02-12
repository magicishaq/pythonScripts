import bs4 #beautifulsoup
import requests
cssSelector = 'a'
url = 'https://developer.mozilla.org/en-US/docs/Web'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elem = soup.select(cssSelector) #list of all he selectors 

hyperlinks = []
for item in elem:
    amazon.append(item.text.strip())

print(hyperlinks)
