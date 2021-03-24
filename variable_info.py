'''
Xavier 
1/03/2020
'''

def getVarName(var): # enter the name of the variable
    varName = list(globals().keys())[list(globals().values()).index(var)]
    return varName


def getFuncName(func):  # Gives us the var name of the function
    x = f'{func}'  # assigns the functions var name but in a format we dont want, such as: (<function test at 0x000001951CF8D840>)
    x = x.split()  # we split it so we can get just the function name easily
    
    return x[1]  # return the function name

def getClassName(cls):  # Gives us the var name of the string
    x = f'{cls}'  # assigns the class name in an unwanted format
    x = x.split()  # we split it so we can get just the class name easier
    x[1] = x[1][10:-1]  # removes the unnessacary '__main__.' from the class name 
    x[1] = x[1][0:-1]  # removes the extra ' 
    
    return x[1]  # return the class name


'''
Usage:

class xgyghb:
    pass

print(getClassName(xgyghb))  # get class name example


def x():
    pass

print(getFuncName(x))  # get func name example


h = 5

print(getVarName(h), "=", h)
'''
