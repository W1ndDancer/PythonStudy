
def CreateNewNames():
    count = 1
    n = ''
    names = {}
    ansCheck = ['y','yes', 'no', 'n']
    answer = 'y'
    while answer == 'y' or answer == 'yes':
        n = input('Name: ')
        names[count] = [n]
        count += 1
        answer = str.lower(input('Add one more?(y,yes,n,no) '))
        while answer not in ansCheck:
            answer = str.lower(input('Add one more?(y,yes,n,no): '))
    else:
        return names

def CreateNewSurnames():
    count = 1
    s = ''
    surnames = {}
    ansCheck = ['y','yes', 'no', 'n']
    answer = 'y'
    while answer == 'y' or answer == 'yes':
        s = input('Surname: ')
        surnames[count] = [s]
        count += 1
        answer = str.lower(input('Add one more?(y,yes,n,no) '))
        while answer not in ansCheck:
            answer = str.lower(input('Add one more?(y,yes,n,no): '))
    else:
        return surnames

def CreateNewBirthdays():
    count = 1
    b = ''
    birthdays = {}
    ansCheck = ['y','yes', 'no', 'n']
    answer = 'y'
    while answer == 'y' or answer == 'yes':
        b = input('Birthday(dd/mm/yyyy): ')
        birthdays[count] = [b]
        count += 1
        answer = str.lower(input('Add one more?(y,yes,n,no) '))
        while answer not in ansCheck:
            answer = str.lower(input('Add one more?(y,yes,n,no): '))
    else:
        return birthdays

def CreateNewTelephones():
    count = 1
    t = ''
    telephones = {}
    ansCheck = ['y','yes', 'no', 'n']
    answer = 'y'
    while answer == 'y' or answer == 'yes':
        t = input('Tel.: ')
        telephones[count] = [t]
        count += 1
        answer = str.lower(input('Add one more?(y,yes,n,no) '))
        while answer not in ansCheck:
            answer = str.lower(input('Add one more?(y,yes,n,no): '))
    else:
        return telephones

def CreateNewAdresses():
    count = 1
    a = ''
    adresses = {}
    ansCheck = ['y','yes', 'no', 'n']
    answer = 'y'
    while answer == 'y' or answer == 'yes':
        a = input('Adress: ')
        adresses[count] = [a]
        count += 1
        answer = str.lower(input('Add one more?(y,yes,n,no) '))
        while answer not in ansCheck:
            answer = str.lower(input('Add one more?(y,yes,n,no): '))
    else:
        return adresses


def initN(x):
    global n
    n = x

def initS(x):
    global s
    s = x

def initB(x):
    global b
    b = x

def initT(x):
    global t
    t = x

def init(x):
    global a
    a = x
