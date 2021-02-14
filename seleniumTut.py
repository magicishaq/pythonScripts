#selenuim allows users to click through webpages
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.google.com/')
import os


#type in inout boxes
searchElm = browser.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
searchElm.send_keys('boxing')
searchElm.submit()
elm = browser.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b')
elm.click()
browser.back() # goes back
broswer.forward() #goes forward
browser.refresh() #refreshes
browser.quit() #closes the browser

#reading the content of the webpages

browser = webdriver.Chrome()
browser.get('https://twistedfood.co.uk/')
headings = browser.find_elements_by_css_selector('h3')
first = headings[0].text
os.chdir('C:\\Users\\ikhan\\Documents\\learningPython\\mockData')
headingFile = open('headings.txt', 'a' )
for i in headings:
    headingFile.write(i.text)

headingFile.close()

