#! python3
import webbrowser, sys, pyperclip
sys.argv #arguments 

#check if command arguments are 

if len(sys.argv) > 1: 
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()
url = 'https://www.google.com/maps/place/' + address
webbrowser.open(url)



