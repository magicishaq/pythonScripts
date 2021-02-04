#! python3
import re, pyperclip

#Create reg ex object for phone numbers
PhoneRegEx = re.compile('''
(
((\d\d\d)|(\(\d\d\d\)))?            #area code (optional)
(\s|-)          #first seperator
\d\d\d            #first 3 digits
-           #seperator
\d\d\d\d            #last 4 digits
(((ext(\.)?\s)|x)    #extension -word part (optional)
(\d{2,5}))?             #extension - number part
)
''', re.VERBOSE)
#TODO: create reg ex for email
EmailRegEx = re.compile(r'''
            #something@somthing.com
[a-zA-Z0-9.+]+            #name part
@            # @ symbol
[a-zA-Z0-9.+]+ #domain name part

''', re.VERBOSE)
#TODO: get text off clipboard
text = pyperclip.paste()
#TODO: extract email/phone from this text
extractedPhone = PhoneRegEx.findall(text)
#TODO: copy the extracted email/phone numbers
extractedEmail = EmailRegEx.findall(text) 

print(extractedEmail)
print(extractedPhone)

