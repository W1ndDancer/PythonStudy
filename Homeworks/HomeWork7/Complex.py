def Calculator(x, y, operation):
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '/':
        result = x / y
    elif operation == '*':
        result = x * y
    return result

def initComplex(a,b,o):
    global x
    global y
    global operation
    x = a
    y = b
    operation = o

def getX():
    x = complex(input('1st expression --> '))
    return x

def getY():
    y = complex(input('2nd expression --> '))
    return y

def getOperation():
    operation = input('operation is --> ')
    return operation
