# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

'''
def CheckIfWeekend(day):
    if (day > 5):
        return f'YES'
    else:
        return f'NO'


print('Today is weekend?')
dayNumber = input('Input day number --> ')

try:
    dayNumber = int(dayNumber)
    if dayNumber > 0 and dayNumber < 8:
        print(CheckIfWeekend(dayNumber))
    else:
        print('WASTED. Number must lay beetwen 1 and 7')
except:
    print('WASTED. U Should enter the number')
'''

# 2.изучить понятие Предкатов. Напишите прог для проверки истиности выраж : !(x or y or z) == !x and !y and !z, для всех значений предикат

'''
def is_right(x,y,z):
    return not(x or y or z) == ((not x) and (not y) and (not z))

x = bool(input('x--> '))
y = bool(input('y--> '))
z = bool(input('z--> '))

print(f'If x = {x}, y = {y}, z = {z}, expression: !(x or y or z) == (!x and !y and !z) is --> {is_right(x,y,z)}')
'''

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

'''
def FindQuater(x, y):
    if x > 0 and y > 0:
        return f'Point lies in 1st quater'
    elif x < 0 and y > 0:
        return f'Point lies in 2nd quater'
    elif x < 0 and y < 0:
        return f'Point lies in 3rd quater'
    elif x > 0 and y < 0:
        return f'Point lies in 4th quater'
    elif x != 0 and y == 0:
        return f'Point lies on the abscissa'
    elif x == 0 and y != 0:
        return f'Point lies on the y-axis'
    else:
        return f'Point lies in center'

x = input('Pls enter X coordinate --> ')
y = input('Pls enter Y coordinate --> ')

try:
    x = float(x)
    y = float(y)
    print(FindQuater(x,y))
except:
    print('WASTED. U should enter NUMBERS!')
'''