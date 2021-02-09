import logging #logging module
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of debugger')

def factorial(n):
    total = 1
    for i in range(1, n+ 1):
        total *= i
return total     
factorial(10)

print('hello')