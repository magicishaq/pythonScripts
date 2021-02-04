# * character means 0 or more times
import re
spidermanRegEx = re.compile(r'Spider(-)*man')
spidermanGroup = spidermanRegEx.search('Spiderman is peter parker')
result = spidermanGroup.group() # match
print(result)
spidermanGroup2 = spidermanRegEx.search('Spider-man loves mary jane')
fo = spidermanGroup2.group()
print(fo)

