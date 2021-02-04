message = 'this is a very long string and it was a long day I will count it'
count = {}
for character in message.upper() : 
    count.setdefault(character, 0) #if there is not a key, create one and set it to one
    count[character] = count[character] + 1 #when the dictionary finds a letter it will add a count to it

print(count)

#Pretty print the module

import pprint
pprint.pprint(count)
#as a string
text = pprint.pformat(count)