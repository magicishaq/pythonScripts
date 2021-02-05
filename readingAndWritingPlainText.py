path = 'C:\\Users\\ikhan\\Documents\\learningPython\\mockData\\hello.txt' #have to use double quotes
helloFile = open(path)
helloFile.read() #can only read once 
content helloFile.read() # can call it multiple times
helloFile.close() 

#readlines
#returns the contents as lines in a list
listHelloFile = helloFile.readlines()
helloFile.close()

#Write mode (override current file )
#if file doesn't exist python will create a new file
#same with append

helloFile = open(path, 'w') #second parameter is w for write
helloFile.write('This text has been modified') #changes the txt file
helloFile.write('Added a second line to the file')
helloFile.close()

#append mode
newPath = path.replace('hello', 'hello2')
helloFile = open(newPath, 'a')
helloFile.write('Created new content')
helloFile.write('More new content')
helloFile.close()

#create new file
import os
os.chdir('C:\\Users\\ikhan\\Documents\\learningPython\\mockData') #changing the location of where the file will be saved to
burgerFile = open('burger.txt', 'w')
burgerFile.write('I Love burgers \n And chips!')
burgerFile.close()

#Storing complex variables using the shelve module
import shelve
shelveFile = shelve.open('myData') #location is based of os.chdir
shelveFile # a dictionary-like data structure
shelveFile['names'] = ['ishaq' , 'fred' , 'batman', 'sunny']
shelveFile.close()

#in the future can open the file and close it, like a dictionary that saves else where
keys = list(shelveFile.keys())
values = list(shelveFile.values())






