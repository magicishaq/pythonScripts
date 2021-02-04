spam = 42 # global

def egg():
    spam = 1 #local
    return spam

egg()
#local scopes cat use variable in another local scope

#globals can be read by local

thing = 'global'
def foo (name):
    thing = 'local'
    print(name + goo(thing))

def goo (num): 
    return num * 4

#changing globals
theBool = False
def changeBool (): 
    global theBool #referenced the global
    theBool = True

print(str(theBool))

