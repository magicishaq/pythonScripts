import re
phoneRegEx = re.compile(r'\d{3}-\d{3}-\d{4}')

resume = 'this is a phone 123-134-1234 and also this 345-555-6666'
allNumbers = phoneRegEx.findall(resume)

print(allNumbers) #list value

digitRegEx = re.compile(r'\d') #any number
lyrics = 'mambp number 5, 12 34 5 come on everybody mambo number 5'

lyricGroup = digitRegEx.findall(lyrics)
print(lyricGroup)

vowelRegEx = re.compile(r'[aeiouAEIOU]') #same as (a|e|i|o|u)
vowelRegEx.findall('robocop eats babay food')

notAVowel = re.comple(r'[^aeiouAEIOU]') #^ means negative

notAVowel.finall(r'this is a grand day')

#starts and ends with
beingsWithHelloRegex = re.compile(r'^hello') #string begins with hello 
endsWithWorldRegex = re.complie(r'world$') #ends with world

isaNumberRegex = (r'^\d+$') #starts with a number and ends with a number
#wildcard character
# . any character except for the newline

#.* means any pattern at all

pattern = 'First name: shaq Last name: bond lol'

nameRegEx = re.compile(r'First name: (.*) Last name: (.*)') #using the .* gets the first name and the last name
group = nameRegEx.findall(pattern) 
print(group)

#.* is greedy, non greefy mode use .*? no greey will find the first match
#example
newPattern = '<h1> Hello world </h1>'
NonGreedyRegex = re.complie(r'<(.*?)>')
print(NonGreedyRegex.findall(newPattern))

#vs greedy

greedyRegex = re.complie(r'<(.*)>')
print (greedyRegex.findall(newPattern)) 


#THE DOT REGEX EXCLUDES THE NEW LINE \n
#HOT TO MAKE THE DOT INCLUDE ALL


dotAllRegex = re.complie(r'.*', re.DOTALL) #second parameter means everything


#CASE insensitive matching

caseRegEx = re.complie(r'[aeiou]', re.IGNORECASE) 


