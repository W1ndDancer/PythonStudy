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

with open ('HW5.txt', 'w') as d:
     d.write(f'{a}\n')
  
SubsList(a)

d.close()
'''

# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66

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
    with open ('HW53.txt', 'w') as d:
        d.write(polySumList)
    

with open ('HW51.txt', 'w') as d1:
     d1.write('2*x^6 + 3*x^5 + 4*x^4 + 7*x^3 + 2*x^2 + 21*x + 4')

with open ('HW52.txt', 'w') as d2:
     d2.write('7*x^7 + 12*x^6 + 63*x^5 - 4*x^4 - 7*x^3 - 5*x^2 - 7*x - 4')
   
data1 = open('HW51.txt', 'r')
data2 = open('HW52.txt', 'r' )

poly = PolySumList(data1, data2)
l = len(poly)
poly = DelZerosFrom(poly, l)
poly = ConvToStrAndSave(poly)

data1.close()
data2.close()