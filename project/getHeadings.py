import bs4, requests
url = 'https://developer.mozilla.org/en-US/docs/Web'
selector = 'h1'
def getHeading(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select(selector)
    headings = []
    for i in elem:
        headings.append(i.text.strip())
    
    return ' \n'.join(headings)
headings = getHeading(url)
print('the headings are ' + headings)