import re #regex module

message = 'this string is a phone number lol 0121-753-0327 0772-472-4920'

phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(message) #finds the first occurance
allPhone = phoneNumRegex.findall(message) #finds all

print(mo.group())

print(allPhone) #list array

