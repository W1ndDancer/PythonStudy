# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

'''
def FactorizeIntoPrime(number):
    factorizedNumber = []
    i = 2
    if number == 1:
        return [1]
    else:
        while number // i != 0:
            if number % i == 0:
                factorizedNumber.append(i)
                number /= i
                i = 2
            else:
                i += 1
        return factorizedNumber

n = input('Input natural integer number to factorize --> ')
try:
    n = int(n)
    if n > 0:
        print(f' {n} = {FactorizeIntoPrime(n)}')
    else:
        print('Number must be greater then 0')
except:
    print('Number must be integer')
'''

# (необязательное) Напишите программу, которая принимает на стандартный вход список игр футбольных команд
#  с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3 
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

'''
from collections import OrderedDict

def ToursResults(totalGamesPlayed):
    matchScore = []
    count = 0
    while count < totalGamesPlayed:
        print(f'tour {count + 1}')
        team1 = str.lower(input('team: '))
        matchScore.append(team1)
        goalsScore1 = int(input('goals scored: '))
        matchScore.append(goalsScore1)
        team2 = str.lower(input('team: '))
        while team2 == team1:
            team2 = str.lower(input('Team 2 must be deffierent. team: '))
        matchScore.append(team2)
        goalsScore2 = int(input('goals scored: '))
        matchScore.append(goalsScore2)
        print('')
        count += 1
    return matchScore

def PointsTable(matchScoreList):
    teamList = []
    games, wins, losses , draws, points = 0, 0, 0, 0, 0

    for i in range(len(matchScoreList)):
        if i % 2 == 0:
            teamList.append(matchScoreList[i])
    teamList = list(OrderedDict.fromkeys(teamList))

    pointsTable = {}
    for j in range(len(teamList)):
        for k in range(0, len(matchScoreList), 2):
            if teamList[j] == matchScoreList[k]:
                games += 1
                if k % 4 == 0: 
                    if matchScoreList[k + 1] > matchScoreList[k + 3]:
                        wins += 1
                        points += 3
                    elif matchScoreList[k + 1] == matchScoreList[k + 3]:
                            draws += 1
                            points += 1
                    else:
                        losses += 1
                else:
                    if matchScoreList[k + 1] > matchScoreList[k - 1]:
                        wins += 1
                        points += 3
                    elif matchScoreList[k + 1] == matchScoreList[k - 1]:
                        draws += 1
                        points += 1
                    else:
                        losses += 1
        pointsTable[f'{teamList[j]}'] = f'G = {games}, W = {wins}, D = {draws}, L = {losses}, P = {points}'
        games, wins, losses , draws, points = 0, 0, 0, 0, 0     
    return pointsTable
    
toursPlayed = int(input('How much tours are played? '))
ourToursResult = ToursResults(toursPlayed)
ourPointsTable = PointsTable(ourToursResult)
for x,y in ourPointsTable.items():
    print(x,y)
    print()

'''


























