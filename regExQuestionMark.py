#! python3 

import re
batRegEx = re.compile(r'Bat(wo)?man') #? = 0 or 1 times
mo = batRegEx.search('The adventures of Batman')
mo.group() #match

wo = batRegEx.search('The adventures of Batwomen')
wo.group() #match

wo2 = batRegEx.search('the adventures of batwowowowoman')
wo2.group() # no match because wo is 0 or 1 times


#phone number capture group to get te area code
phoneRegEx = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneGroup = phoneRegEx.search('123-1234-12345') 
phoneGroup.group() # has a match
secondPhoneGroup = phoneRegEx.searach('no area code 234-2345')
secondPhoneGroup.group() #has a match also

#\? to capture regex


