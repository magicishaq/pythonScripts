#upper and lower
spam = 'hello world' 
spam.upper()
spam.upper()

spam.isupper() #bool
spam.islower() #bool
#needs letters

#chanining 
spam.upper().isupper()

spam.isupper() #letters only
spam.islnum() #letters and numbers only
spam.isdecimal() #numbers only
spam.isspace() #whitespace only
spam.istitle() #titlecase only first letter is capital, other is lowercase
spam.title() # turns to title


spam.startswith('i') #can be a longer string
spam.endswith('q') #can be a longer case

','.join(['h', 'e', 'l', 'l', 'o']) #what is joining the array (list together) 
'my name is isaq'.split() #end of string to turn into array, default is space


'my name is ishaq'.splt('m') #spilts on m

'ishaq'.rjust(10) #total length is 10 .. white space pads to the right
'ishaq'.ljust(10) # same but padding on left

'ishaq'.rjust(10, '8') #padding is 8
'ishaq'.center(10, '*') #centers it

'    ishaq    '.strip() # removes white space
'   sihaq    '.lstrip() # left side remove
'    isjahkh    '.rstrip() #right side

thing = '123ishaq123'.strip('123') #removes the characters passed into the argument


print(thing)
'111111hello'.replace('111', '!') #replaces first strng with second parameter

#pyperclip 


