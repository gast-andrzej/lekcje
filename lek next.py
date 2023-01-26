'''
Rozgrzewka




'''
import string
#
#
# def func2():
#     z = open("textowka.txt", "r")
#     b = list()
#     g = 0
#     ff = list(string.ascii_uppercase)
#     for i in z:
#         for j in i:
#             b.append(j)
#     for i in b:
#         if i in ff:
#             g = g+1
#         else:
#             pass
#
#     print(g)

# func2()

#
# def func3():
#     z = open("textowka.txt", "r")
#     b = []
#     g = 1
#     for i in z:
#         for j in i:
#             b.append(j)
#     for i in b:
#         if i == "\n":
#             g = g+1
#     print(g)
#
# func3()
'''
Napisz funkcje która tworzy plik .py i napisze w nim cosia który po wywołaniu powie "Hello World!" :)

'''

import os # for windows
import subprocess # for normal operation system :)
#
# def func1():
#     z = open("plikerniacz.py", "a")
#     z.write(f'print("Hello World!")')
#     z.close()
#     os.system()
#
#
# func1()
'''
zadanie 1
napisz mi funkcje która tworzy plik tekstowy i system windows go uruchamia :)

'''

# def func1():
#     z = open("teksty.txt", "w")
#     z.write("hello")
#     z.close()
#     os.startfile("teksty.txt")

# func1()

#
# def func1():
#     b = open("textowka.txt", "r")
#     z = []
#     for i in b:
#         for j in i:
#             z.append(j)
#     # print(z)
#     print(z.count("a"))
#
#
# func1()






def func2():
    x = input("co chcesz odpalić? "
              "1 - plik textowy"
              "2 - plik excelowy"
              "3 - plik doc")
    '''
    1 - plik textowy
    2 - plik excelowy
    3 - plik doc
    '''
    try:
        int(x)
        match x:
            case "1":
                z = open("pliktxt.txt", "a")
                z.close()
                subprocess.run("pliktxt.txt")
            case "2":
                z = open("plikexcelowy.xlsx")
                z.close()
                os.startfile("plikexcelowy.xlsx")
            case "3":
                z = open("plikdoc.docx")
                z.close()
                os.startfile("plikdoc.docx")
    except:
        print("wprowadź liczbę")

# func2()

import sys



# subprocess.call(["pliktxt.txt"], shell=True)







