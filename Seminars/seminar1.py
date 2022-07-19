# TASK 1. Найти сумму 2х чисел. Числа вводятся пользователем.

# def Summ(a,b):
#     summAB = a + b
#     return summAB

# x = (input('input 1st number --> '))
# try:
#     x = int(x)
# except:
#     print('U should input INT number')
# y = int(input('input 2nd number --> '))
# summXY = Summ(x,y)
# print(f'Summ is {summXY}')

# TASK 2. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# def CheckIfSquare(a, b):
#     if (a*a == b):
#      return f'The 1st number is equal to square of the 2nd'
#     elif (b*b == a):
#      return f'The 2nd number is equal to square of the 1st'
#     else:
#      return f'Numbers is not equal to sqaure of each other'

# x = int(input('input 1st number --> '))
# y = int(input('input 2nd number --> '))

# print(CheckIfSquare(x,y))

# TASK 3. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

'''
def FindMaxNumber(numbers):
    max = numbers[0]
    count = 0
    for i in numbers:
        if (max < i):
            max = i
    return max

def FillListWithINT(numbers):
    count = 0
    while count < len(numbers):
        numbers[count] = int(input(f'intput {count} number --> '))
        count +=1
    return numbers

def CreateListOfZeros(size):
    listofzeros = [0]*size
    return listofzeros

size = int(input('How much numbers do U wanna enter? '))
numbers = CreateListOfZeros(size)
numbers = FillListWithINT(numbers)
maxNumberInList = FindMaxNumber(numbers)
print(f'Max number is --> {maxNumberInList}')
'''

# TASK 4. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

'''
def showINTnumbersInRange(n):
    r = range(-n,n+1)
    for i in r:
        print(i, end=' ')
try:
    number = int(input('Input number --> '))
    showINTnumbersInRange(number)
except:
    print('U should enter INT number. Retry')
'''

# TASK 5. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

'''
def Show1stDigitOfFraction(number):
    if (number/(int(number)) == 1):
        return print('Number is integer and has no fraction part')
    else:
        remainder = abs(number) % 1
        firstDigit = int(remainder*10)
        return print(firstDigit)


x = float(input('Input number --> '))
Show1stDigitOfFraction(x)
'''

# TASK 6. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

'''
def CheckNumberIFMultiple(number):
    if number//5 == 1 and number//10 == 1 or number//15 == 1 and number//30 != 1 :
        return print(True)
    else:
        return print(False)

n = int(input('Input number --> '))
print('Is number multiple to 5 and 10 or to 15 and number is not miltiple to 30?')
CheckNumberIFMultiple(n)
'''