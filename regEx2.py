#! python3



import re
message = '111-111-1111'
phoneRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegEx.search(message)
firstGroup = mo.group(1); 
secondGroup = mo.group(2)
wholeGroup = mo.group()

#quit() 
#using or , the pip
batRegEx = re.compile(r'Bat(man|mobile|bike|copter|bat)')
batString = 'Batman get to the Batcopter and grab the Batmobile, while you  are there Batbat and away!'
foo = batRegEx.search(batString)
print(foo.group())







