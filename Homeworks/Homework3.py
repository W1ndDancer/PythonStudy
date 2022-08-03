# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

'''
def CreateAndFillList():
    someList = []
    size = int(input('Input size of ur list --> '))
    for i in range(size):
        someList.append(someList)
        someList[i] = input(f'Input {i} element --> ')
    return someList

def DeterminateIfContains(someList, someElement):
    for i in range(len(someList)):
        if someList[i] == str(someElement):
            return True
        elif someList[i] != someElement and i == len(someList) - 1:
            return False

listForTask = CreateAndFillList()
print(listForTask)
searchingElement = input('input number to determinate if its in list --> ')
try:
    searchingElement = int(searchingElement)
    print(DeterminateIfContains(listForTask, searchingElement))
except:
    print('U should enter an integer number')
'''

# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def DeterminateSecondOccurrence(someList, elementToDerminate):
    count = 0
    for i in range(len(someList)):
        if someList[i] == elementToDerminate and count == 1:
            return i
        elif someList[i] == elementToDerminate:
            count += 1
        elif someList[i] != elementToDerminate and i == len(someList) - 1:
            return -1

listForTask = []
print(f'Our list is {listForTask}')
elementToFind = "123"
print(f'Searching: {elementToFind}')

if listForTask == []:
    print('List is empty. Position is --> -1')
else:
    print(f'Position  of 2nd occurrence is --> {DeterminateSecondOccurrence(listForTask, elementToFind)}')


# 3* (необзательная).
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
#  в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
# Sample Input 2:
# a A a
# Sample Output 2:
# a 3

'''
import re

def CountWords(text):
    text = str.lower(text.replace('.',','))
    text = str.lower(text.replace(' , ',' '))
    listFromText = re.split(' |, |,| , ', text)
    listOfUniqWordsFromText = list(set(listFromText))
    count = 0
    dictionaryResult = {}
    for i in range(len(listOfUniqWordsFromText)):
        for k in range(len(listFromText)):
            if listOfUniqWordsFromText[i] == listFromText[k]:
                count += 1
                dictionaryResult[listOfUniqWordsFromText[i]] = count
        count = 0
    dictionaryResult['Total amount of words'] = len(listFromText)

    return dictionaryResult

someText = 'Привет привет мопед дед, кадет.привет мопед,или Дед а может кадет или может привет. Все же ПРИВЕТ КАДЕТ или МоПед,а дед оказался кадет . который сЕл на моПед'

dict = CountWords(someText)
for x,y in dict.items():
    print(f'{x} --> {y}')
'''