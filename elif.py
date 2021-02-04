name = 'zak'
age = 3000
if name == 'zak':
    print('hello zak')
elif age < 12 : 
    print('too young kiddo')
elif age > 2000: 
    print('nice try but zak is not an immortal')
elif age > 100: 
    print('you are really old')


#Truthy, falsey values

print('Enter your name')
name = input(); 
if name: 
    print('thank you for entering a name')
else: 
    print('you did not enter a name')

#works because a string is truthy
#0 is falsey and so is 0.0

bool(1) #will turn this truthy

bool('') #falsey
bool('hello world') #truthy value
