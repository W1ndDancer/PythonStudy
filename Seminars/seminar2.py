# Напишите прог для проверки истиности выраж : !(x or y or z) == !x and !y and !z, для всех значений предикат

'''
def is_right(x,y,z):
    return not(x or y or z) == ((not x) and (not y) and (not z))

x = bool(input('x--> '))
y = bool(input('y--> '))
z = bool(input('z--> '))

print(f'If x = {x}, y = {y}, z = {z}, expression: !(x or y or z) == (!x and !y and !z) is --> {is_right(x,y,z)}')
'''

#  Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

'''
def FindDistanceIn2DSpace(x1,y1,x2,y2):
    distance = ((x2 - x1)**2 - (y2 - y1)**2)**0.5
    return round(distance, 2)

xA = float(input('input X coordinate of point A --> '))
yA = float(input('input Y coordinate of point A --> '))
xB = float(input('input X coordinate of point B --> '))
yB = float(input('input Y coordinate of point B --> '))

print(FindDistanceIn2DSpace(xA,yA,xB,yB))
'''

# В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу,
#  по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".
# Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
# Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное),
#  выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
#  для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
# В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

'''
def DeclinationProgramist(number, word):

    temp = number // 10
    temp2 = number % 100
    temp3 = number - 10 * temp

    if temp3 >= 1 and temp3 < 5 and temp2 > 10 and temp2 < 15:
        return f'{number} {word}ов'
    elif temp3 == 1:
       return f'{number} {word}'
    elif temp3 > 1 and temp3 < 5:
        return f'{number} {word}а'
    else:
        return f'{number} {word}ов'

w = 'программист'
n = 5000011

print(DeclinationProgramist(n, w))
'''

# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

'''
def Subsequence(number):
    numbersSubsequence = list(range(0, number))
    print(numbersSubsequence)
    for i in numbersSubsequence:
        if i % 2 == 0:
            numbersSubsequence[i] = 3**i
        else:
            numbersSubsequence[i] = -3**i
    return numbersSubsequence


N = input('How much numbers in subsequence do u need? Pls enter --> ')
try:
    N = int(N)
    print(Subsequence(N))
except:
    print('Pls enter int number')
'''

# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число,
#  второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

'''
def SimpleCalculator(x, y, operation):
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '/':
        result = x / y
    elif operation == '*':
        result = x * y
    elif operation == 'mod':
        result = x % y
    elif operation == 'pow':
        result = x ** y
    elif operation == 'div':
        result = x // y
    return round(result,3)

x = float(input('1st number --> '))
y = float(input('2nd number --> '))
operation = str.lower((input('operation is --> ')))

if y == 0 and operation == '/':
    print('Division by zero!')
else:
    print(SimpleCalculator(x, y, operation))
'''

# КНБ - вы играете с ботом, варианты раунда игры - победа 1 очко, проигрыш 0 очков, ничья 0.5 балла
# Чтоб статистика сохранялась, и можно было играть неограниченное количество раундов

'''
import random

def RPS(playerScore, computerScore):
    rpsList = ['rock', 'papper', 'scissors']
    print('Rock, Papper or Scissors?')
    playerChoice = str.lower(input('Enter ur choice --> '))
    while playerChoice not in rpsList:
        print('Retry')
        playerChoice = str.lower(input('Enter ur choice --> '))    
    computerChoice = random.choice(rpsList)
    print(f'Computer choice is --> {computerChoice}')

    if playerChoice == computerChoice:
        print('Draw in this round!')
        GplayerScore = 0.5
        GcomputerScore = 0.5
    elif ((playerChoice == 'rock' and computerChoice == 'scissors') or 
          (playerChoice == 'papper' and computerChoice == 'rock') or 
          (playerChoice == 'scissors' and computerChoice == 'papper')):
        print('You won this round!')
        GplayerScore = 1
        GcomputerScore = 0
    else:
        print('You lost this round!')
        GplayerScore = 0
        GcomputerScore = 1

    print('')
    wannaPlay = str.lower(input('One more game? Pls enter "yes" or "no": '))
    if wannaPlay == 'yes':
        playerScore.append(GplayerScore)
        computerScore.append(GcomputerScore)
        RPS(playerScore, computerScore)
    elif wannaPlay == 'no':
        playerScore.append(GplayerScore)
        computerScore.append(GcomputerScore)
        totalPlayerScore = sum(playerScore)
        totalComputerScore = sum(computerScore)

        print(f'You:      {playerScore}')
        print(f'Computer: {computerScore}')
        print('')
        print(f'Ur total score is {totalPlayerScore} and computer total score is {totalComputerScore}')
        if totalPlayerScore > totalComputerScore:
            return print('U WIN A WAR!')
        elif totalComputerScore > totalPlayerScore:
            return print('U LOOSE A WAR :(')
        else:
            return print('DRAW. WE WILL FIND WHO IS BETTER NEXT TIME.')

    while wannaPlay != ('yes' or 'no'):
        wannaPlay = str.lower(input('ERROR. PLS ENTER ONLY "YES" OR "NO" --> '))
        if wannaPlay == 'yes':
            playerScore.append(GplayerScore)
            computerScore.append(GcomputerScore)
            RPS(playerScore, computerScore)
        elif wannaPlay == 'no':
            playerScore.append(GplayerScore)
            computerScore.append(GcomputerScore)
            totalPlayerScore = sum(playerScore)
            totalComputerScore = sum(computerScore)

            print(f'You:      {playerScore}')
            print(f'Computer: {computerScore}')
            print('')
            print(f'Ur total score is {totalPlayerScore} and computer total score is {totalComputerScore}')
            if totalPlayerScore > totalComputerScore:
                return print('U WIN A WAR!')
            elif totalComputerScore > totalPlayerScore:
                return print('U LOOSE A WAR :(')
            else:
                return print('DRAW. WE WILL FIND WHO IS BETTER NEXT TIME.')

playerScore = []
computerScore = []
RPS(playerScore, computerScore)

'''