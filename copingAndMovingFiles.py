import shutil
#copy file to a new folder
fromLocation = ''
toLocation = ''
shutil.copy(fromLocation, toLocation + 'filename.extension') #adding a filename will rename the copied file

#copy a whole folder
fromLocationofFolder = ''
toLocationofFolder = ''
shutil.copytree(fromLocationofFolder, toLocationofFolder)

#move file to newLocation

fromLocal = ''
toLocal = '' 
shutil.move(fromLocal, toLocal)


#moving to same place, but changing the extention of the file, will rename the file


