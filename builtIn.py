import random
theNumber = random.randint(1,10) #random int between 1 10

while theNumber != 7:
    print(theNumber)
    theNumber = random.randint(1,10)


import sys, os, math
from random import * #when doing this you have access to the properties without calling random. 
randint(1,100) #didnt need random. part

print('hello')
#how to terminate a program early
sys.exit()
print('bye') #wont execute because sys.exit() was called!
