import requests, os
jekyll = 'https://www.gutenberg.org/files/42/42.txt' 
res = requests.get(jekyll) #contains the response
res.status_code #200 means everything is okay
res.text #whole copy of text

print(res.text[:500])
os.chdir('C:\\Users\\ikhan\\Documents\\learningPython\\mockData')
try:
    res.raise_for_status()
    playFile = open('drJandH.txt' , 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except:
    print('Invalid')