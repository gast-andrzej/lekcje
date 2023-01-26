'''
PRACA DOMOWA
'''
import random
import string
#
#
# def func1():
#     liczba1 = random.randint(1000,9999)
#     liczba2 = 5489
#     b = str(liczba1)
#     z = str(liczba2)
#     g1 = []
#     g2 = []
#     b.split()
#     z.split()
#     for i in b:
#         g1.append(i)
#     for i in z:
#         g2.append(i)
#     print(g1)
#     print(g2)
#     indexer = 1
#     for i in g1:
#         if i in g2:
#             print(f"element {indexer} którym jest {i} jest")
#         indexer = indexer+1
#
# # func1()
#
#
#
#
# def func2():
#     return list(range(0,100))
#
# def func3():
#     return list(string.ascii_letters)
#
# def func4():
#     z = func2()
#     y = func3()
#     x = []
#     for i in range(0,10):
#         indexer = random.randint(1,101)
#         if indexer % 2 == 0:
#             x.append(z[random.randint(0,int(len(z))-1)])
#         else:
#             x.append(y[random.randint(0,int(len(y))-1)])
#     return print(x)
#
# # func4()
#
#
#
import pandas

'''
Praca z różnymi plikami w pythonie

formaty
'''


'''
LEK1
.txt
.csv
'''
#
# def func1():
#     b = open("texter.txt", "a", encoding="UTF-8")
#     z = ["Tom", "Bob", "Mark", "Brian", "Dżesika", "Mary"]
#     for i in z:
#         b.write(f"Hello {i}\n")
#
#
#
# func1()
#
import pandas as pd
import xlwt



def func1():
    df = open("addresses.csv", "r")
    b = open("texter.txt", "a")
    for i in df:
        b.write(i)

# func1()










'''
LEK2
.xls
.xlsx

LEK3
.doc
.docx
.pdf


LEK4
.py

LEK5
Generatory
.py

LEK6
Algorytmy

'''

