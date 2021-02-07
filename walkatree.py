#walking a dir tree
import os
import shutil
theWalk = os.walk('C:\\Users\\ikhan\\Documents\\JavascriptTutorial')
for folderName, subFolders, filenames in theWalk:
    print('folder is' + folderName)
    print('the subfolder ' + str(subFolders))
    print('and the filename ' + str(filenames))
    #loop through items
    for subFolder in subFolders:
        if 'extension' in subFolder:
            #os.rmdir(subFolder) #removes item

    for filename in filenames:
        if filename.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, filename + 'back-up')) #makes a copy


