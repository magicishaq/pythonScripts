#function to guess the number
import random #random module

print('Guess te number')
name = input()#gets the name

print('Im am thinking of a number ' + name)
sercretNumber = random.randint(1,20)

for i in range(1,10):
    print('take a guess')
    guess = int(input())
    if guess == sercretNumber:
        print('Correct')
        break
    else:
        print('Wrong, try again')

print('thank you for playing')