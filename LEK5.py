# import string
#
# inputer = "Hello World"
#
# def func1(inputer):
#     mix = []
#     terry = []
#     for i in string.ascii_letters:
#         mix.append(i)
#     for i in range(0, len(mix)-1):
#         terry.append(i)
#     matrix = dict(zip(mix, terry))
#     for i in inputer.split():
#
#
#
#
#
# func1()


'''
WYJĄTKI
'''
#
# x = "Hello"
#
# try:
#     int(x)
#     if int(x) >= 5:
#         print("Hello")
#     else:
#         print("Nope")
#
# except ValueError:
#     print("Tylko liczby")

# j = [3,2,6,4,8,9,5,"Hello", "OH NO", 0.6]
#
# def func1(j):
#     bugs = 0
#     finish = 0
#     succcess = 0
#     for i in j:
#         try:
#             int(i)
#             if int(i) == 5:
#                 # print("Access")
#                 finish = finish+1
#                 succcess = succcess+1
#             else:
#                 # print("Block")
#                 finish = finish+1
#         except ValueError:
#             bugs = bugs+1
#             # print("Numbers")
#     print(f"FINISH CODE {finish}")
#     print(f"FINISH CODE WITH SUCCESS {succcess}")
#     print(f"ERRORS {bugs}")
#
# func1(j)
#



'''
jaki element wprowadzony wolimy?

tupla
'''

import string
import random

'''
wyrzuci mi liste losowych liter (małych i dużych (w formacie UTF-8 / w standardzie qwerty)) oraz losowych cyfr od 0 do 100
'''

def func1(n):
    list_str = []
    list_num = []
    random_list = []
    for i in string.ascii_letters:
        list_str.append(i)
    for i in range(0,101):
        list_num.append(i)
    for i in range(0,n):
        indexer = random.randint(0,1)
        match indexer:
            case 0:
                random_list.append(list_str[random.randint(0,len(list_str)-1)])
            case 1:
                random_list.append(list_num[random.randint(0,len(list_num)-1)])

    print(random_list)


# func1(50)


fixer = [8, 28, 'O', 'R', 80, 'A', 'w', 51, 'y', 97, 76, 14, 48, 'H', 52, 94, 'W'
    , 'B', 'Q', 'p', 43, 'g', 'P', 'R', 'Q', 52, 27, 66, 26, 33, 53, 'Y', 95, 98
    , 'M', 'a', 28, 15, 'g', 93, 86, 36, 70, 27, 'V', 'D', 'm', 'B', 30, 82]

'''
Czy każda z tych liczb jest większa od 50 i parzysta, a jeśli nie to czy jest parzysta czy większa, przechwyć wyjątki :)

output wyjątku -> litera <nasza litera> nie jest liczbą, zatem nie spełnia warunków, wyjątek wynika z <nazwa wyjątku>
'''

def func2(fixer):
    for i in fixer:
        try:
            int(i)
        #     MODULO %
            if int(i) >= 50 and int(i) % 2 == 0:
                print("Trafiony, zatopiony")
            elif int(i) >= 50:
                print("Tylko większy")
            elif int(i) % 2 == 0:
                print("Tylko parzysty")
            else:
                print("Liczba mniejsza od 50 i nie parzysta")
        except ValueError:
            print(f"litera {i} nie jest liczbą, zatem nie spełnia warunków, wyjątek wynika z Value Error")

func2(fixer)


'''
ZAD DOMOWE

Mastermind

wybór jednej liczby i podpowiedzi czy jest ona parzysta, czy mniejsza czy większa czy podzielna przez 7 i próbujesz trafić
liczbę wybraną przez komputer w 10 próbach 

zad z * 
dodaj przechwyt wyjątków do masterminda nie resetujący próby 

'''