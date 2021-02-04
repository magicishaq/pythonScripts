import re
namesRegex = re.compile(r'Mr \w+') #matches Mr and a word character
pattern = 'Mr Smith and Mrs Smtih went to the park, Dr Jones sat at home. Mr Khan was playing playstation while Mr Pink was watching the tv '
allMr = namesRegex.findall(pattern) 
print(allMr) 

#sub method replaces the occurance of the regex with first argument, second is the pattern
newPattern = namesRegex.sub('Master', pattern )


#Now instead of changing the whole name, Will will get a part of the string and replace it

namesRegex = re.compile(r'Mr (\w)\w+') # grabing the first letter of the name
allHidden = namesRegex.sub(r'Agent \1****', pattern) #using the \1 is a placeholder for the group



