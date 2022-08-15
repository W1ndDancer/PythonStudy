# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''
def RLEcoding(strToConv):
    res = ''
    count = 1
    for i in range(len(strToConv) - 1):
        if strToConv[i] == strToConv[i+1] and i < len(strToConv) - 2:
            count += 1
        elif strToConv[i] == strToConv[i+1] and i == len(strToConv) - 2:
            count += 1
            res += str(count) + strToConv[i]
        elif strToConv[i] != strToConv[i+1] and i == len(strToConv) - 2:
            res += str(count) + strToConv[i]
            count = 1
            res += str(count) + strToConv[i+1]
        else:
            res += str(count) + strToConv[i]
            count = 1

    return res

def RLEdecoding(codedStr):
    result = ''
    count = 0
    for i in range(len(codedStr)):
        if codedStr[i].isdigit() == True:
            count = count*10 + int(codedStr[i])
            if i == len(codedStr)-1:
                result+= codedStr[i-1] * int(count)
        else:
            result+= codedStr[i] * int(count)
            count = 0    
    return result
        
with open('HW6.txt', 'w') as data:
    data.write('aaaAAAnnVVVkccccccccccccccccccAAdddds')
data = open('HW6.txt', 'r')
for line in data:
    res = RLEcoding(line)
data = open('HW61.txt', 'w')
data.write(f'{RLEcoding(line)}\n{RLEdecoding(res)}')
data.close()
'''
# 41. Создайте программу для игры в "Крестики-нолики".

'''
import random

def X0(gt, choices, whosTurn, xor0):
    if whosTurn % 2 == 0:
        pl = str.lower(input('ur choice: '))
        while pl not in choices:
            pl = str.lower(input('Wrong choice, pls repeat: : '))
            if pl == 'q':
                return print('U quit')
        if xor0 == 0:
            gt[(choices[pl]//10)][(choices[pl]%10)] = 'X'
        else:
            gt[(choices[pl]//10)][(choices[pl]%10)] = '0'
        del(choices[pl])
    else:
        bot = random.choice(list(choices))
        if xor0 == 1:
            gt[(choices[bot]//10)][(choices[bot]%10)] = 'X'
        else:
            gt[(choices[bot]//10)][(choices[bot]%10)] = '0'
        del(choices[bot])
    print()
    for i in range(len(gt)):
        for j in range((len(gt[i]))):
            print (gt[i][j], end = ' ')
        print()

    a = WinCheck(gt)
    if a == 1 and whosTurn % 2 == 0:
        return print(f'U Win!')
    elif a == -1 and whosTurn == xor0 + 8:
        return print(f'Draw!')
    elif a == 1 and whosTurn % 2 == 1:
        return print(f'PC Wins!')
    elif a == -1:
        X0(gt, choices, whosTurn+1, xor0)

def WinCheck(gt):
    if ((gt[0][0] == 'X' and gt[0][1] == 'X' and gt[0][2] == 'X') or
    (gt[1][0] == 'X' and gt[1][1] == 'X' and gt[1][2] == 'X') or
    (gt[2][0] == 'X' and gt[2][1] == 'X' and gt[2][2] == 'X') or
    (gt[0][0] == 'X' and gt[1][0] == 'X' and gt[2][0] == 'X') or
    (gt[0][1] == 'X' and gt[1][1] == 'X' and gt[2][1] == 'X') or
    (gt[0][2] == 'X' and gt[1][2] == 'X' and gt[2][2] == 'X') or
    (gt[0][0] == 'X' and gt[1][1] == 'X' and gt[2][2] == 'X') or
    (gt[0][2] == 'X' and gt[1][1] == 'X' and gt[2][0] == 'X') or
    (gt[0][0] == '0' and gt[0][1] == '0' and gt[0][2] == '0') or
    (gt[1][0] == '0' and gt[1][1] == '0' and gt[1][2] == '0') or
    (gt[2][0] == '0' and gt[2][1] == '0' and gt[2][2] == '0') or
    (gt[0][0] == '0' and gt[1][0] == '0' and gt[2][0] == '0') or
    (gt[0][1] == '0' and gt[1][1] == '0' and gt[2][1] == '0') or
    (gt[0][2] == '0' and gt[1][2] == '0' and gt[2][2] == '0') or
    (gt[0][0] == '0' and gt[1][1] == '0' and gt[2][2] == '0') or
    (gt[0][2] == '0' and gt[1][1] == '0' and gt[2][0] == '0')):
        return 1
    else:
        return -1

startChoices = {
        'tl': 0, 'tm': 1, 'tr': 2,
        'ml': 10, 'm': 11, 'mr': 12,
        'bl': 20, 'bm': 21, 'br': 22
                }
gt = [['_']*3 for i in range(3)]

print('To put X or 0 in some place ur should enter:\n\n' + 
'tl - top left corner; tm - top middle; tr - top right corner;\n' +
'ml - middle left; m - middle; mr - middle right\n' +
'bl - bottom left corner; bm - bottom middle; br - bottom right corner\n' +
'q  - to quit. When playing u should enter "q" 2 times\n')

xor0 = str.lower(input('Attention X always makes 1st turn.\nDo u wanna play with X or 0? '))
whosTurn = 0
while xor0 not in ['x', '0', 'q']:
    xor0 = str.lower(input('U did smt wrong.\nU should enter X or 0. Repeat:  '))
else:
    if xor0 == 'x':
        xor0 = 0
        whosTurn = 0
        X0(gt, startChoices, whosTurn, xor0)
    elif xor0 == 'q':
        print('U quit')
    else:
        xor0 = 1
        whosTurn = 1
        X0(gt, startChoices, whosTurn, xor0)
'''

# 41. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:* 
# 1+2*3 => 7; 
# (1+2)*3 => 9;

'''
def Convert(equation):
    equation = list(equation)
    convEqv = []
    numb = 0
    for i in range(len(equation)):
        if equation[i].isdigit() and i != len(equation) - 1:
            numb = numb*10 + float(equation[i])
        elif equation[i].isdigit() and i == len(equation) - 1:
            numb = numb*10 + float(equation[i])
            convEqv.append(numb)
        else:
            convEqv.append(numb)
            convEqv.append(equation[i])
            numb = 0
    return convEqv
    
def FindOperAmount(equation):
    count = 0
    equation = list(equation)
    for i in equation:
        if i == '*' or i == '/' or i == '+' or i == '-':
            count += 1
    return count

def CalcPro2(x, operationAmount):
    opList = ['*', '/', '-', '+']
    operation = 0
    ind = 0
    opCount = 0
    print(x)
    for i in range(len(opList)):
        for j in range(len(opList)):
            for l in range(len(x)):
                if (opList[j] == '*') and (x[l] == '*') and (opCount == 0):
                    operation = x[l-1] * x[l+1]
                    x[l-1] = operation
                    ind = l
                    opCount+=1
                elif( opList[j] == '/') and (x[l] == '/') and (opCount == 0):
                    if x[l+1] == 0:                            
                        return f'Division by 0!!!'
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
        CalcPro2(x, operationAmount - 1)
    else:
        return print(f'answer --> {x[0]}')

a = input('Enter expression --> ')
conv = Convert(a)
opCount = FindOperAmount(a)
c = CalcPro2(conv, opCount)
'''
