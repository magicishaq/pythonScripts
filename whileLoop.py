#while loop 

spam = 0
while spam < 5: 
    print('hello world')
    spam = spam + 1


name = ''
while name != 'your name': 
    print('Please type your name')
    name = input()
print('thank you')

#or
thing = ''
while True:
    print('Type in your age')
    thing = input()
    if thing == 'your age':
        break
print('thank you, please come again')

