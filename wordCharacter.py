import re
namesRegex = re.compile(r'Mr \w+') #matches Mr and a word character
pattern = 'Mr Smith and Mrs Smtih went to the park, Dr Jones sat at home. Mr Khan was playing playstation while Mr Pink was watching the tv '
allMr = namesRegex.findall(pattern) 
print(allMr) 


