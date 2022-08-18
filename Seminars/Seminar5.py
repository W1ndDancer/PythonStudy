# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

'''
from typing import OrderedDict

someList = [1, 2, 4, 2, 4, 45, 0, 0, 18, 7, 6, 2]

print(list(set(someList)))
print(list(OrderedDict.fromkeys(someList)))

'''
# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

'''
import random

def CreatePolynomial(polPow):

    numbSignList = ['+', '-']
    numbSignListStart = ['', '-']
    polynomial = random.choice(numbSignListStart)
    for i in range(polPow, 0, -1):
        if i == 1:
            polynomial += f'{random.randint(0,100)}*x {random.choice(numbSignList)} '
        else:
            polynomial += f'{random.randint(0,100)}*x^{i} {random.choice(numbSignList)} '

    polynomial += f'{random.randint(0,100)} = 0'
    return polynomial

k = int(input('k = '))
while k < 1:
    k = int(input('!!! k >= 1 !!! k = '))
polynomialForTask = CreatePolynomial(k)

with open ('fileS5.txt', 'w') as data:
    data.write(polynomialForTask)
'''

# 34. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

'''
def PolySumList(pol1, pol2):
    for line1 in pol1:
        line1 = line1.replace(' + ', ' ')
        line1 = line1.replace(' - ', ' -')
        line1 = line1.replace('*', ' *')
        line1 += ' *x^0'
        line1 = line1.split()
    for line2 in pol2:
        line2 = line2.replace(' + ', ' ')
        line2 = line2.replace(' - ', ' -')
        line2 = line2.replace('*', ' *')
        line2 += ' *x^0'
        line2 = line2.split()

    if len(line1) > len(line2):
        line3 = line1 + line2
    else:
        line3 = line2 + line1
    for i in range(0, len(line3), 2):
        line3[i] = int(line3[i])

    delPos = 0
    for k in range(1, len(line3) - 2, 2):
        if line3[k] == '*x^0' and delPos == 0:
            delPos = k
        for l in range(k + 2, len(line3), 2):
            if line3[k] == line3[l]:
                line3[k - 1] += line3[l - 1]
        line3[k - 1] = str(line3[k - 1])
    del line3[delPos:len(line3) - 1]
    
    return line3

def DelZerosFrom(polySumList, lenPolyList):
    for m in range(lenPolyList-1):
        if polySumList[m] == '0':
            del polySumList[m:m + 2]
            return DelZerosFrom(polySumList, lenPolyList - 2)
        elif m == lenPolyList - 2:
            return polySumList
            
def ConvToStrAndSave(polySumList):
    polySumList = ' '.join(polySumList)
    polySumList = polySumList.replace(' *', '*')
    polySumList = polySumList.replace(' ', ' + ')
    polySumList = polySumList.replace(' + -', ' - ')
    with open ('fileS52.txt', 'w') as d:
        d.write(polySumList)
    

data1 = open('fileS5.txt', 'r')
data2 = open('fileS51.txt', 'r' )

poly = PolySumList(data1, data2)
l = len(poly)
poly = DelZerosFrom(poly, l)
poly = ConvToStrAndSave(poly)

data1.close()
data2.close()
'''

# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

'''
def FindMissingNumber(listSubs):
    for i in range(1, len(listSubs)):
        if (listSubs[i] - 1) != listSubs[i - 1]:
            searchingNumb = listSubs[i] - 1
            return searchingNumb
        if i == len(listSubs) - 1 and (listSubs[i] - 1) == listSubs[i - 1]:
            return f'Evrything OK'

def OpenAndConvToList():
    with open ('fileS53.txt', 'r') as data:
        for line in data:
            line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])
        return line

subs = OpenAndConvToList()
print(f'Missing number is --> {FindMissingNumber(subs)}')
'''

# 1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

'''
def SubsList(someList):
    newList = []
    max = someList[0]
    for i in range(len(someList) - 1):
        newList.append(someList[i])
        for k in range(i, len(someList)):
            if someList[k] > max:
                newList.append(someList[k])
                max = someList[k]
                if len(newList) > 1:
                    with open('HW5.txt', 'a') as data:
                        data.write(f'{newList}\n')
            if someList[k] > someList[i] and someList[k] != max:
                if max in newList:
                    newList.pop()
                newList.append(someList[k])
                if len(newList) > 1:
                    with open('HW5.txt', 'a') as data:
                        data.write(f'{newList}\n')
            
        max = someList[i+1]
        newList = []

a = [1, 5, 2, 3, 4, 6, 1, 7]
SubsList(a)
'''

# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв"

'''
def DelWordsForFragment(words):
    newWords = []
    fragment = 'абв'
    words = words.split()
    for word in words:
        if fragment not in word:
            newWords.append(word)
    ' '.join(newWords)
    return newWords

abc = 'абвыв ароа арыл фьабв апоо абвабв'

print(DelWordsForFragment(abc))
'''
