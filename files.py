#! python3
templatePath = r'C:\Users\ikhan\Documents\JavascriptTutorial'
otherPath = r'C:\Users\ikhan\Downloads'
import os
filepath = os.path.join('c:', 'documents', 'example.png') #this creates a file path that will be modified for the operating system it is on
print(filepath) 
cd = os.getcwd(); 

#os.chdir('c:\\') #changes the directory

#absolute filepath, begins with the root folder (complete location)
#relative path, relative to the working directory
# .\ folder, this directory
#..\ means parent folder


#turn  a relative path into a absolute path
abPath = os.path.abspath('files.py')
abPathPArent = os.path.abspath('..\\')

#check for ab or relative
isThisAb = os.path.isabs(otherPath) # returns bool
theRelPath = os.path.relpath(otherPath, templatePath ) #starting point first arguent, the destination second argument

#just the direction part without the file
dirPath = os.path.dirname(templatePath + r'\index.html')

#pulls out the last part of the path
basename = os.path.basename(templatePath)
os.path.exists(templatePath) #checks if this filename is correct
#is a file
os.path.isdir(templatePath)
#is a directory
os.path.isfile(templatePath)
#tells how big a file is
size = os.path.getsize(templatePath + r'\index.html')
print(size)

#tells what files are in a folder
listOfFiles = os.listdir(templatePath) #returns list
