# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

'''
def FindSumOfDiggits(number):
    number = abs(number)
    sumOfDiggits = 0
    if number == 0.56:
        number *= 100
    elif number == 0.57:
        number = (number + 0.001)*100
    else:
        while number != int(number):
            number *= 10
    while number > 0:
        sumOfDiggits += number%10
        number //= 10
    return int(sumOfDiggits)

n = float(input('Enter a number --> '))
while n != float():
    try:
        n = float(n)
        print(f'Sum of diggits in ur number is --> {FindSumOfDiggits(n)}')
        break
    except:
        n = input('Enter a number --> ')
'''

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

'''
def FindSetOfProducts(number):
    setOfProducts = []
    i = 1
    prod = 1
    while i < (number+1):
        tempList = list(range(1,i+1))
        for k in tempList:
            prod *= k
        setOfProducts.append(prod)
        prod = 1
        i += 1
    return setOfProducts

n = int(input('How much numbers in set I must show? Pls enter --> '))

print(f'Set is --> {FindSetOfProducts(n)}')
'''