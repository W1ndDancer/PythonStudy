def CreateNew():
    count = 1
    n, s, t, a, d = '', '', '', ''
    phonebook = {}
    ansCheck = ['y','yes', 'no', 'n']
    answer = 'y'
    while answer == 'y' or answer == 'yes':
        n = input('Name: ')
        s = input('Surname: ')
        t = input('Tel.: ')
        a = input('Adress: ')
        phonebook[f'{count}.'] = f'NS: {n} {s};\n   Tel: {t};\n   Comment: {c};\n'
        count += 1
        answer = str.lower(input('Add one more?(y,yes,n,no) '))
        while answer not in ansCheck:
            answer = str.lower(input('Add one more?(y,yes,n,no): '))
    else:
        return phonebook

def ImportExisting():
    return 1

# phonebook1 = CreateNew()

# for x,y in phonebook1.items():
#     print(x,y)
#     print()
