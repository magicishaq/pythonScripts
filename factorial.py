import logging #logging module
logging.disable(logging.CRITICAL) #diables the logging 
logging.basicConfig(level=logging.DEBUG, force=True, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of debugger')

def factorial(n):
    logging.debug('this is the start of te function %s' % (n))
    total = 1
    for i in range(1, n+ 1):
        total *= i
        #logging.debug('the total %s and the value of n %s'% (total, n))
    return total     
factorial(10)


print('hello')



