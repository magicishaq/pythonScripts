#dictionary are basically objects, can store different data types
diction = {'key': 'value', 'second': 'the value'}
diction['key']
#dictionary arwe unordered

#check if key exsits

'key' in diction #True
'key' not in diction # False

#get the keys
list(diction.keys()) #keys
list(diction.values()) #values
list(diction.items()) #key , vlaue pai in tuples

#looping through all the keys in a dicionay
for key in diction.keys():
    print(key)

#multiple assignment trick
for key,value in diction.item():
    print(key, value)

#check if dictionary has a key
eggs = {'size' : 'large', 'color' : 'orange' , 'calories' : '67' } 
if 'size' in eggs: 
    print(eggs['size'])
#this is long, alternative is

#get method
eggs.get('color' , 0 ) #first parameter gets the value, if it doesn't exsit, falls on the secodn argument

#if the dictionary doesnt have a key, set it with a value
eggs.setdefault('brand', 'asda') 
eggs.setdefault('brand', 'tesco') #wont change because the default was already set







