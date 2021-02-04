#functions
def hello () :
    print('hello world')


hello() 
hello()
hello()

def greeting(string):
    print(string)

greeting('hello world')

def plusOne(number):
    return number + 1

def doubleit(number):
    return number * 2

def doubleitPlusOne(number):
    return plusOne(doubleit(number))
#None value
None #datatype that represents a lack of a value, will not display to the shell
#every function call has a return value
#if the return keyword is not used the default value is None


#Keyword arguments
print('hello', end='null') #the end keyword refers to a new line created by the print, this can be replaced by changing the arugment

print('i','khan', sep = "^^^^^^___^^^^^^") #changes the separator keyword




 