#an array called a list

spam = ['dog', 'cat', 'rat', 'elephant']

spam[0] #dog

foo = [[1,2,3],['one', 'two', 'three']]

foo[0] # 1,2,3
foo[0][1] # 1

foo[-1] #last item in the list
foo[-2] #second to last item in the list

for i in range(0,len(spam)):
    item = spam[i]
    print(item)

spam[1:3] #splice, starts at 1 ends in 3 , returns that sub array

thing = ['hello', '3', 10]
thing[0] = 'new input'
thing # new input, 3 , 10

thing[0:2] = ['cat', 'dog', 'mouse'] #replacing the current selection

newArr = [1,2,3,4,5] 
newArr[1:] #leaving a side blank means the end
newArr[:3] #start

del newArr[0] #deletes from the list
[1,2,3] + [4,5,6] # [1,2,3,4,5,6]
[1] * 3 # [1,1,1]
list('Hi') #['H', 'i'], doesnt work with ints

'thing' in ['thing', 'hello'] #checks if in a list
#True

1 not in [1,2,3,4] #returns the opposite



