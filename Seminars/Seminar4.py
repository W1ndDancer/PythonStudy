# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''
def FindSumOfOddElements(someList):
    sum = 0
    for i in range(1, len(someList), 2):
        sum += someList[i]
    return sum

listForTask = [2, 3, 5, 9, 3]
print(FindSumOfOddElements(listForTask))
'''

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

'''
def FindProductOfPairElements(someList):
    if len(someList) % 2 == 0:
        listOfProducts = [1]*(len(someList)//2)
        for i in range(len(listOfProducts)):
            listOfProducts[i] = someList[i]*someList[(len(someList) - 1 - i)]
        return listOfProducts
    else:
        listOfProducts = [1]*(len(someList)//2 + 1)
        for i in range(len(listOfProducts)):
            listOfProducts[i] = someList[i]*someList[(len(someList) - 1 - i)]
        return listOfProducts

listForTask = [2, 3, 4, 5, 6]
print(FindProductOfPairElements(listForTask))
'''

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.001, 10.01] => 0.2

'''
def FindDifferenceOfFractionalParts(someList):
    for i in range(len(someList)):
        someList[i] = someList[i] % 1
    diff = max(someList) - min(someList)
    return round(diff, 3)
        
listForTask = [1.1, 1.2, 3.1, 5.001, 10.01]
print(FindDifferenceOfFractionalParts(listForTask))
'''

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

'''
def ConvertDecimalToBinary(number):
    binaryNumber = []
    basisOfNumbSyst = 2
    if number == 0:
        return 0
    else:
        while abs(number) > 0:
            number = abs(number)
            remainder = number % basisOfNumbSyst
            binaryNumber.insert(0, remainder)
            number //= basisOfNumbSyst
        return binaryNumber

n = -6
binNumList = ConvertDecimalToBinary(n)
for i in binNumList:
    print(i, end = ' ')
'''

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = -8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1,

'''
def Fibonacci (elCount):
    fibonacciList = [1, 1]
    elementsRange = range(2, abs(elCount))
    if elCount == 1 or elCount == -1:
        fibonacciList = [1]
        return fibonacciList
    elif elCount > 1:
        for i in elementsRange:
            fi = fibonacciList[i - 2] + fibonacciList[i - 1]
            fibonacciList.append(fi)
        return fibonacciList
    elif elCount < -1:
        for k in elementsRange:
            fk = fibonacciList[k - 2] + fibonacciList[k - 1]
            fibonacciList.append(fk)
        for l in range(len(fibonacciList)):
            if l % 2 != 0:
                fibonacciList[l] *= -1
        for j in range(len(fibonacciList)//2):
            fibonacciList[len(fibonacciList) - j - 1], fibonacciList[j] = fibonacciList[j], fibonacciList[len(fibonacciList) - j - 1]
        return fibonacciList
    else:
        return 0

n = -8
print(Fibonacci(n))
'''

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

'''
def FindMaxMinNum(someString):
    listFromSomeString = someString.split(' ')
    result = (max(listFromSomeString), min(listFromSomeString))
    return result

stringForTask = '67 6 54 2 6 23 12 1'
maxMin = FindMaxMinNum(stringForTask)
print(f'Max = {maxMin[0]}, Min = {maxMin[1]}')
'''

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python

'''
def FindRootsOfQuadEquation(a, b, c):
    discr = b**2 - 4*a*c
    if discr > 0:
        x1= (-b + discr**0.5)/(2*a)
        x2= (-b - discr**0.5)/(2*a)
        return (x1, x2)
    elif discr == 0:
        x = -(b/(2*a))
        return x
    else:
        return f'Roots not exist'

a = 2
b = 0
c = -2
print(FindRootsOfQuadEquation(a, b, c))
'''

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

'''
import math

def FindLeastCommonMultiple(number1, number2):
    for i in range(1, number1*number2 + 1):
        if (i % number1) == 0 and (i % number2) == 0:
            return i
            
n1 = 3
n2 = 7
print(FindLeastCommonMultiple(n1, n2))
print(math.lcm(n1,n2))
'''