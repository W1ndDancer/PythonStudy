
import datetime

def init(c):
    global choice
    choice = c

def getChoice():
    choice = int(input('Ur choice --> '))
    return choice

def showResultC1(x, y, operation, result):
    dayMonth = datetime.datetime.today().strftime("%d.%m")
    HourMin = datetime.datetime.today().strftime("%H:%M")
    with open('/Users/wind/Desktop/Study/6. Python/Homeworks/HomeWork7/LogFile.txt', 'a') as log:
        log.write(f'{dayMonth} {HourMin}: {x} {operation} {y} = {result}\n')
        print(f'{x} {operation} {y} = {result}')
        log.close()

def showResultC2(x, conv):
    dayMonth = datetime.datetime.today().strftime("%d.%m")
    HourMin = datetime.datetime.today().strftime("%H:%M")
    with open('/Users/wind/Desktop/Study/6. Python/Homeworks/HomeWork7/LogFile.txt', 'a') as log:
        log.write(f'{dayMonth} {HourMin}: {x} = {conv[0]}\n')
        print(f'{x} = {conv[0]}')
        log.close()

def showResultC3():
    dayMonth = datetime.datetime.today().strftime("%d.%m")
    HourMin = datetime.datetime.today().strftime("%H:%M")
    log = open('/Users/wind/Desktop/Study/6. Python/Homeworks/HomeWork7/LogFile.txt', 'a')
    log.write(f'{dayMonth} {HourMin}: Log opened\n')
    log.close()
    log = open('/Users/wind/Desktop/Study/6. Python/Homeworks/HomeWork7/LogFile.txt', 'r')
    for line in log: 
        print(line)
    log.close()

def showResultC4():
    dayMonth = datetime.datetime.today().strftime("%d.%m")
    HourMin = datetime.datetime.today().strftime("%H:%M")
    with open('/Users/wind/Desktop/Study/6. Python/Homeworks/HomeWork7/LogFile.txt', 'a') as log:
        log.write(f'{dayMonth} {HourMin}: Calc closed\n')
        print('U quit')
        log.close()

