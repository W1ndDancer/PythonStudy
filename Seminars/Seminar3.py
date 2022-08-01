'''
sp=[5,11,2,3,4,8,157,555]
def max_average(sp):
    maxx=sp[0]
    sr=0
    for i in sp:
        if i > maxx:
            maxx=i
            sr+=i
    sr=sr/len(sp)
    rez={}
    rez['максимальный элемент']=maxx
    rez['среднее арифметическое']=sr
    k=(maxx,sr,rez)
    return k

res=max_average(sp)
#print(res[2])
for x,y in res[2].items():
    print(x,y)

'''
# print(len(rez))
# for x,y in rez.items():
# print(x,y)
'''
'''

# Задать список из n чисел последовательности фибоначи и вывести их сумму на экран

# VAR 1
'''
def Fibonacci (number):
    fibonacciList = [0, 1]
    numbersRange = range(2, number + 1)
    i = 2
    if number == 0:
        fibonacciList = [0]
        sumFib = sum(fibonacciList)
        return (sumFib, fibonacciList)
    elif number == 1:
        sumFib = sum(fibonacciList)
        return (sumFib, fibonacciList)
    elif number > 1:
        for i in numbersRange:
            fi = fibonacciList[i - 2] + fibonacciList[i - 1]
            fibonacciList.append(fi)
            sumFib = sum(fibonacciList)
        return (sumFib, fibonacciList)
    else:
        return f'Fibonacci list not exist'

n = 10
fib = Fibonacci(n)
print(f'List = {fib[1]}')
print(f'Sum = {fib[0]}')
'''
# VAR 2

'''
def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibolist(x):
    list = []
    for i in range(1, x+1):
        list.append(fibo(i))
    return list

x = int(input('Введите число элементов: '))
print(fibolist(x))
'''

# Написать программу которая на вход принимает список, а возвращает назад словарь со следующими значениями: max, min, max и min индексы и сред арифм.

'''
def TakeListReturnDictionary(someList):
    maxInList = someList[0]
    minInList = someList[0]
    countIdx = range(0, len(someList) + 1)
    maxIdx = 0
    minIdx = countIdx[0]
    average = round(sum(someList)/len(someList), 2)
    for i in range(len(someList)):
        if someList[i] > maxInList:
            maxInList = someList[i]
            maxIdx = i
        if someList[i] < minInList:
            minInList = someList[i]
            minIdx = i
    dictionaryResult = {}
    dictionaryResult['Max element'] = maxInList
    dictionaryResult['Min element'] = minInList
    dictionaryResult['Max index'] = maxIdx
    dictionaryResult['MinIndex'] = minIdx
    dictionaryResult['Average'] = average
    return dictionaryResult

lis = [0, 1, 15, 4, 3, 3, 2]

dict = TakeListReturnDictionary(lis)
for x,y in dict.items():
    print(x,y)
'''

#  ВАР 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. сохраните список в формате JSON.

'''
import json

def CreateListOfNumbers(elementsCount):
    listOfNumbers = list(range(-elementsCount, elementsCount + 1))
    return listOfNumbers

listForTask = CreateListOfNumbers(10)

with open('data.json', 'w', encoding = 'utf-8') as outfile:
    outfile.write(json.dumps(listForTask, ensure_ascii = False))
    # indent = 1 - отступ. Так в файл json запишутся все элементы с новой строки с указаным отступом.
print('json file is saved')

with open('data.json', 'r', encoding = 'utf-8') as outfile:
    listN = json.load(outfile)

print(listN)
'''

#  ВАР 2. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найти произведение указанных элементов. Элементы указаны в текстовом файле,
#         в отдной строке - одно число

'''
def CreateListOfNumbers(elementsCount):
    listOfNumbers = list(range(-elementsCount, elementsCount + 1))
    return listOfNumbers

# with open('fileS3.txt', 'w') as data:
#     data.write('1\n')
#     data.write('3\n')

listT = CreateListOfNumbers(3)
print(listT)

multiple = 1
dataForTask = open('fileS3.txt', 'r')
for line in dataForTask:
    multiple *= listT[int(line)]
print(multiple)
'''