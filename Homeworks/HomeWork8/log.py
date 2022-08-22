import json


def SaveFile(n,s,b,t,a):
    with open('data1.json', 'w', encoding = 'utf-8') as outfile:
        outfile.write(json.dumps(n, ensure_ascii = False))
    with open('data2.json', 'w', encoding = 'utf-8') as outfile:
        outfile.write(json.dumps(s, ensure_ascii = False))
    with open('data3.json', 'w', encoding = 'utf-8') as outfile:
        outfile.write(json.dumps(b, ensure_ascii = False))
    with open('data4.json', 'w', encoding = 'utf-8') as outfile:
        outfile.write(json.dumps(t, ensure_ascii = False))
    with open('data5.json', 'w', encoding = 'utf-8') as outfile:
        outfile.write(json.dumps(a, ensure_ascii = False))

def LoadFileN():
    with open('data1.json', 'r', encoding = 'utf-8') as outfile:
            n = json.load(outfile)
            return n

def LoadFileS():
    with open('data2.json', 'r', encoding = 'utf-8') as outfile:
            s = json.load(outfile)
            return s

def LoadFileB():
    with open('data3.json', 'r', encoding = 'utf-8') as outfile:
            b = json.load(outfile)
            return b

def LoadFileT():
    with open('data4.json', 'r', encoding = 'utf-8') as outfile:
            t = json.load(outfile)
            return t

def LoadFileA():
    with open('data5.json', 'r', encoding = 'utf-8') as outfile:
            a = json.load(outfile)
            return a



# n = {1: ['Val'], 2:['Iry']}
# s = {1: ['Bryk'], 2:['Bryksina']}
# b = {1: ['12.08'], 2:['20.07']}
# t = {1: ['420'], 2:['428']}
# a = {1: ['Ostrava'], 2:['OstravaM']}

# # path = '/Users/wind/Desktop/Study/6. Python/Homeworks/HomeWork8/data.json'
# # with open(path, 'r', encoding = 'utf-8') as outfile:
# #             listN = json.load(outfile)
# #             print(listN)

# print(LoadFileA())
# # print(SaveFile(n,s,b,t,a))
