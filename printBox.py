#finding the bugs
#own custom message
#raise Exception('this is a custom message')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('width and height have to greater than 1')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol )
    
    print(symbol * width)


boxPrint('*', 20, 20)
boxPrint (')' , 20, 2 )

