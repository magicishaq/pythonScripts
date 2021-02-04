import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#using verbose mode means the regex string can have white space but it doesnt count
pnVerboseRegex = re.compile(r'''
\d\d\d #can even add comments
-\d\d\d-
\d\d\d\d
''', re.VERBOSE)
#using BITWISE OPERATORS
#what if you wanted to ignore case, use verbose and have the dot character mean everything
bitwiseRegex = re.compile(r'.*?', re.DOTALL | re.IGNORECASE | re.VERBOSE) #use the bitwise in the second parameter for everything

