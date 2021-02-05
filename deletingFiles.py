import os
for filename in os.listdir():
    if filename.ends('.rxt'):
        print(filename) 
#can stop you from deleting the wrong file

#deleting files
#1 

filename = ''
filepath = ''
os.unlink(filename) #perma delete

#2 remove directory
os.rmdir(filepath) #only if empty

#3 to delete a folder and everything inside
import shutil
shutil.rmtree(filepath) #perma deletes, wont be in the recylcing bin

#install = 'py -m pip install -U send2trash'
import send2trash #sends to the recycling bin
send2trash.send2trash(filename) # sends to the recycling bin


