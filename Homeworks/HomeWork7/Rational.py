from lib2to3.pytree import convert


def Convert(x):
    x = list(x)
    convEqv = []
    index = []
    numb = 0
    stop = 0
    f = 0
    for i in range(len(x)):
        if x[i].isdigit() and i != len(x) - 1:
            numb = numb*10 + float(x[i])
        elif x[i].isdigit() and i == len(x) - 1:
            numb = numb*10 + float(x[i])
            convEqv.append(numb)
        else:
            convEqv.append(numb)
            convEqv.append(x[i])
            numb = 0
    for j in range(len(convEqv)):
        if convEqv[j] == '.' or convEqv[j] == ',':
            f = convEqv[j+1]
            while f > 1:
                f/=10
            c = convEqv[j-1] + f
            convEqv[j-1] = c
            index.append(j)
    for k in range(0, (2*len(index)),2):
        for l in index:
            if stop == 0:
                del convEqv[l-k:l+2-k]
                stop += 1
        index.pop(0)
        stop = 0
    return convEqv

def FindOperAmount(conEqv):
    count = 0
    conEqv = list(conEqv)
    for i in conEqv:
        if i == '*' or i == '/' or i == '+' or i == '-':
            count += 1
    return count

def CalcPRO(x, operationAmount):
    opList = ['(', ')', '*', '/', '-', '+']
    operation, ind, opCount, bktOpn, bktCls = 0, 0, 0, 0, 0
    for i in range(len(opList)):
        if ('(' in x) and (')' in x):
            for m in range(len(x)):
                if x[m] == '(':
                    bktOpn = m
                elif x[m] == ')':
                    bktCls = m
            for n in range(bktOpn+1, bktCls):
                if (opList[i] == '*') and (x[n] == '*') and (opCount == 0):
                    operation = x[n-1] * x[n+1]
                    x[n-1] = operation
                    ind = n
                    opCount+=1
                elif( opList[i] == '/') and (x[n] == '/') and (opCount == 0):
                    if x[n+1] == 0:
                        return f'Division by 0!!!'
                    else:
                        operation = x[n-1] / x[n+1]
                        x[n-1] = operation
                        ind = n
                        opCount+=1
                elif (opList[i] == '-') and (x[n] == '-') and (opCount == 0):
                    operation = x[n-1] - x[n+1]
                    x[n-1] = operation
                    ind = n
                    opCount+=1
                elif (opList[i] == '+') and (x[n] == '+') and (opCount == 0):
                    operation = x[n-1] + x[n+1]
                    x[n-1] = operation
                    ind = n
                    opCount+=1
                elif (bktCls == n + 1) and (bktOpn == (n - 1)):
                    del x[n+1:n+3]
                    del x[n-2:n]
        elif ('(' in x) and (')' not in x):
            return f'Mistake in expression. U have missed --> )'
        elif (')' in x ) and ('(' not in x):
            return f'Mistake in expression. U have missed --> ('
        else:
            for j in range(len(opList)):
                for l in range(len(x)):
                    if (opList[j] == '*') and (x[l] == '*') and (opCount == 0):
                        operation = x[l-1] * x[l+1]
                        x[l-1] = operation
                        ind = l
                        opCount+=1
                    elif( opList[j] == '/') and (x[l] == '/') and (opCount == 0):
                        if x[l+1] == 0:
                            return 'Division by 0!!!'
                        else:
                            operation = x[l-1] / x[l+1]
                            x[l-1] = operation
                            ind = l
                            opCount+=1
                    elif (opList[j] == '-') and (x[l] == '-') and (opCount == 0):
                        operation = x[l-1] - x[l+1]
                        x[l-1] = operation
                        ind = l
                        opCount+=1
                    elif (opList[j] == '+') and (x[l] == '+') and (opCount == 0):
                        operation = x[l-1] + x[l+1]
                        x[l-1] = operation
                        ind = l
                        opCount+=1
    del x[ind:ind+2]
    if operationAmount > 1:
        CalcPRO(x, operationAmount - 1)


def getX():
    x = input('Enter expression --> ')
    return x

def initRational(a):
    global x
    x = a

def initRes(r):
    global result
    result = r

