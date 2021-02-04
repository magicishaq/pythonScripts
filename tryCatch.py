def divideBy42 (dividBy):
    try:
        return 42/dividBy
    except ZeroDivisionError:
        print('error you tried dividing by 0')

print(divideBy42(100))
print(divideBy42(2))
print(divideBy42(20))
print(divideBy42(200))
print(divideBy42(0))

def example (num): 
    try: 
        num - 6
    except: 
        print('not right')


example('ishaq')
example(10)
example(True)

#using try catch in if statement
def howManyCats():
    try: 
        print('how many cats')
        numCats = input()
        if int(numCats) >= 5:
            print('thats allot of cats')
        elif int(numCats) < 0:
            print('Sorry must be a positive number')
        else:
            print('thats not allot')
    except ValueError:
        print('sorry please input a number')


howManyCats()


