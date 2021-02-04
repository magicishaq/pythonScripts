# + character means one or more
import re

supermanRegEx = re.compile(r'Super(man|dog)+!')
supermanGroup = supermanRegEx.search('Superman! and Superdog! will match, but super! will not, also Supermanmanman will match')
print(supermanGroup.group(1))


#specific number of repitions
laughRegex = re.compile(r'Ha{3}')
laughGroup = laughRegex.search('HaHaHa - what you laughing at')

#range
cryRegEx = re.compile(r'Bo{1,4}') #Bo 1 to 4 times

#regex is greedy, will find the longest possible match
#non greedy {4,6}?   using question will find the shortest possible match
