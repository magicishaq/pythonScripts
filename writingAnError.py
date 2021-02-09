#change the directory to mockData folder
import os
os.chdir(os.getcwd() + '\\mockData')
os.getcwd()
#recording the error message
import traceback
try: 
    raise Exception('this is the error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc()) #appends the error message to the log
    errorFile.close()

#Assertion is an insanity check is the check fails, raise an exception
assert False, 'this is the error message' #if asserts to fault print error message
