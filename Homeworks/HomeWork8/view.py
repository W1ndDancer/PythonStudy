def getChoice():
    choice = int(input('Ur choice --> '))
    return choice

def newDB():
    return print('New DB is created and saved')

def Quit():
    return print('U quit')

def init(c):
    global choice
    choice = c

def PrintInfo(n,s,b,t,a):
    answer = input('Options: f - full; n - names, s - surnames, b - birthdays, t - telephones, a - adresses\n Ur option: ')
    while answer not in ['f','n', 's', 'b', 't', 'a']:
        answer = input('u did smr wrong, pls tryagain. Ur option: ')
    if answer == 'f':
        for k, v in s.items():
            if k in n:
                n[k].extend(v)
            else:
                n[k] = v
        for k, v in b.items():
            if k in n:                
                n[k].extend(v)
            else:
                n[k] = v
        for k, v in t.items():
            if k in n:
                n[k].extend(v)
            else:
                n[k] = v
        for k, v in a.items():
            if k in n:
                n[k].extend(v)
            else:
                n[k] = v
        print(n)
    if answer == 'n':
        for k,v in n.items():
            print (k,v)
    if answer == 's':
        for k,v in s.items():
            print (k,v)
    if answer == 'b':
        for k,v in b.items():
            print (k,v)
    if answer == 't':
        for k,v in t.items():
            print (k,v)
    if answer == 'a':
        for k,v in a.items():
            print (k,v)