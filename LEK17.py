# import string

#
# class dictionar:
#
#     def func1(self = None):
#         return list(range(1,101))
#
#     def func2(self = None):
#         return list(string.ascii_letters)
#
#     def func3(self=None):
#         return dict(zip(dictionar.func1(),dictionar.func2()))
#
#     def __init__(self):
#         dictionar.func3()
#
#
# dictionar()
import random

#
# class obiekt:
#
#     def generator(self=None):
#         gg = ["Adam", "Mikołaj", "Andrzej", "Tomek", "Kasia", "Paweł", "Piotrek", "Zenek"]
#         index = random.randint(0,len(gg)-1)
#         dane = [gg[index], random.randint(20,60)]
#         yield dane
#
#
# def func1():
#     lista = []
#     for i in range(0,100):
#         lista.append(next(obiekt.generator()))
#     return lista
#
#
#


'''
MASTERMIND
'''

def mastermind():
    glownaliczba = random.randint(1000,9999)
    indexer = 15
    while indexer > 0:
        x = input("podaj liczbę ")
        try:
            int(x)
            gracz = int(x)

            if glownaliczba == gracz:
                print("Koniec, Congratulation")
                break

            if glownaliczba % 2 == 0:
                print("liczba jest parzysta")



            if gracz > glownaliczba:
                print("liczba jest większa od wytypowanej")
            elif gracz < glownaliczba:
                print("liczba jest mniejsza od wytypowanej")





            indexer = indexer - 1
        except:
            print("podaj liczbę !!")
    print(glownaliczba)

mastermind()


'''
        tutaj mastermind

        - podpowiedź jeśli liczba parzysta i podana przez gracza też parzysta powiedzieć, że liczba główna jest parzysta

        - podpowiedź liczba jest większa lub mniejsza od podanej przez gracza

        - poszczególne elementy wew są identyczne (4 składowe np. g 1111   docelowa 5421) mówi, ostatnia liczba jest taka sama

        - liczba główna jest podzielna przez sumę cyfr liczby gracza bądź przez 7

        - liczba jest liczbą pierwszą bądź nie


        ma pokazywać ile prób ci zostało :)

        ma reagować tylko na int, gdy gracz wprowadzi string gra ma mu wytknąć błąd ale nie uznawać tej próby
'''







