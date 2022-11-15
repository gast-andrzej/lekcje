#
# # import random
# # import string
# #
# #
# # # TABLICE
# # #
# # # lista_produktow = ['lody', 'ciastka', 'cukierki', 'gofry', 'chleb', 'masło', 'napoje']
# # #
# # #
# # # def func1():
# # #     u = int(len(lista_produktow))
# # #     lista_numerow = list(range(1, u+1))
# # #     b = dict(zip(lista_numerow,lista_produktow))
# # #     print(b)
# # #
# # #
# # # func1()
# #
# # def func1(x):
# #     strlista = []
# #     randomlista = []
# #     for elem in string.ascii_letters:
# #         strlista.append(elem)
# #     for i in range(0,x):
# #         randomlista.append(strlista[random.randint(0,len(strlista)-1)])
# #     print(randomlista)
# #     print(randomlista[len(randomlista)-1])
#
#
# # func1(30)
#
# # def func2():
# #     for i in range(0,30):
# #         print(i*"😃")
# #
# # func2()
# #
# # def func2():
# #     for i in range(0,20):
# #         print(f'{" "*(i+10)}'"*"*i)
# #
# # func2()
#
#
# # def func1():
# #     lista1 = ["owoce","warzywa","mleko"]
# #     lista2 = ["ser", "szynka", "jajka"]
# #     lista3 = []
# #     for i in lista1:
# #         lista3.append(i)
# #     print(lista3)
# #
# # func1()
#
#
#
# '''
# SKRÓTY
#
# len() - długość elementu
# range(x, y) - zasięg liczbowy od x do y (wszystkie liczby)
# append - dodawanie elementu do listy
# pop - wyrzucenie ostatniego elementu z listy
# for i in range(0,10):   -->    DLA i(elementów) w przedziale liczbowym od 0 do 10 (dla każdej z tych liczb) wykonaj
# biblioteka random
#
#
# '''
#
#
#
# '''
#
#
# # '''
# # lista_imion = ["Adam", "Tomek", "Bartek", "Michał"]
# #
# # def func1(x):
# #     for i in x:
# #         if i.upper() == "TOMEK" or i.upper() == "MICHAŁ":
# #             # print(i + " Możesz wejść")
# #             print(f"{i} Możesz wejść")
# #         else:
# #             # print(i + " Nieautoryzowany dostęp")
# #             print(f"{i} Nieautoryzowany dostęp")
# #
# #
# # func1(lista_imion)
#
#
# # b = range(0,100)
# #
# # def func1(b):
# #     '''
# #     Chciałbym by element przyjęty przez func1, został przetworzony na listę :)
# #     '''
# #     n = []
# #     # for i in b:
# #     #     n.append(i)
# #     n = list(b)
# #     print(n)
# #
# # func1(b)
#
# b = [1,2,3,4,5,6,7,8,9]
#
# def func1():
#     gg = 0
#     for i in b:
#         gg = gg+i
#         print(gg)
#     print(gg)
# func1()
#
#
# '''
# NAPISZ 3 funkcje które przetwarzają listy dodając je
#
# 1 do pustej listy
# 2 do listy częściowo zajętej ( lista = ["Hello", "World", "1111"])
# 3 dodawać elementy do listy wprowadzonej (lista wprowadzona = ["!", "Hello"]) po przejściu ma wyglądać tak
# ["!", "Hello", "A", "B", "C"])
#
# Napisz 3 funkcje które porównują elementy z list wprowadzonych czy są one parzyste czy nieparzyste, czy są mniejsze czy
# większe od x, czy są napisane z małych czy dużych liter.
# '''
#
# '''
#
# '''