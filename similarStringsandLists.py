#things you can do with strings and lists

name = 'ishaq'
name[0] #i
name [:1] #shaq
'is' in name # True
for letter in name: 
    print(letter) # i s h a q


#lists are mutable (can be changed) 
#string are immutable and therefore only overidden

#changing a string
sentence = 'The dog jumped over the fence'
newSentence = 'Mr' + sentence[3:] 
print(newSentence)

#lists are references
#to make a deep copy
import copy
copy.deepcopy([1,2,3]) # made a deep copy
#lists can span multiple lines 
aList = ['hello'
'john']

#use \ character to carry on to new line
print('this line will be very I want to continue on a new line' + \
    'and it will here')



