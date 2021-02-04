#! python3
#will return the files and file size of items in a foler
import os
total = 0
pathName = r'C:\Users\ikhan'
for filename in os.listdir(pathName):
    if not os.path.isfile(os.path.join(pathName, filename)):
        continue #skips the folder
    else: 
        total = total + os.path.getsize(os.path.join(pathName, filename))


print(total)
