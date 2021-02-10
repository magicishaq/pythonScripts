import logging #logging module

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')


#logging levels
logging.debug()
loging.info()
logging.warning()
logging.error()
logging.critical() #highest level

#write to a text file
logging.basicConfig(filename='logThiserror.txt', level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#added filename parameter

