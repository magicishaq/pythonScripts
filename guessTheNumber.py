import random
print('Hello what is you name')
name = input()
print('Well' + str(name) + ' Im thinking of a number between 1 and 20')
print('Can you guess the number?')
print('You ave 7 attempts')

#guess the number function
def guessNumber (): 
    secretNumber = random.randint(1,20)
    start = 1
    end = 8 
    for guessesTaken in range(start,end):
        print('take a guess?')
        guess = int(input())
        if guess < secretNumber:
            print('guess is too low. You have ' + str(end - guessesTaken) )
        elif guess > secretNumber:
             print('guess is too High. You have ' + str(end - guessesTaken) )
        else: 
            break #correct number guessed

    if guess == secretNumber:
        print('Good job: The Number I ws thinking was' + str(secretNumber) + 'Nice work' + name)
    else: 
        print('sorry wrong number, I was thinking of' + str(secretNumber))



guessNumber()