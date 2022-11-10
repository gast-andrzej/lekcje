# # '''
# # Listy, tuple, pętla for, zakresy
# # '''
# #
# # lista1 = [1,2,3,7,5,3,2] # typy w liście to int
# # lista2 = ['h','e','l', "HELLO",1,'looooo World'] # typy w liście to string
# # lista3 = [1,2,3,'hello','world'] # brak określonego typu danych
# #
# # print(len(lista1))
# #
# # lista1.append('hello')
# #
# # # print(lista1.pop())
# # print(lista1[len(lista1)-1])
# #
# # # len liczy dane w taki sposób elem1, elem2, elem3
# # # to dla niego 1,2,3 czyli razem 3
# # # natomiast pierwszy element listy to 0
# # # czyli lista złożona z elem1, elem2, elem3 -> jej ostatni element to 2
# # # bo lista zaczyna liczyć od zera 0, 1, 2 :)
# # # obejściem tego problemu jest -1 :D print(lista1[len(lista1)-1])
# #
# # print(len(lista1)) #dane które udostępnia len to postać INT
# #
# # print(lista1[::-1]) #kod do obrócenia listy :)
# #
# #
# # '''
# # typy danych takie jak stos - LIFO
# #
# # elem1, elem2, elem3
# #
# # od ostatniego elementu są wyciągane
# #
# #
# # First In First Out - ZASADA FIFO
# #
# # elem1, elem2, elem3
# #
# # pierwsze weszło, pierwsze wyszło
# #
# #
# # First In Last Out - FILO
# # żeby zapobiec wyciekowi danych
# # '''
# #
# # '''
# # DZIAŁANIA Z LISTAMI STR
# # '''
# #
# # print(lista2)
# # # zamień listę na napis h e l lo World
# #
# # lista2.pop()
# # lista2.append("lo World")
# # print(lista2)
# # listaduze = []
# # listamale = []
# # listarozne = []
# # lista_z = []
# # lista_int = []
# # lista2 = ['h','e',7, 15, 'l', "HELLO",1,'looooo World', 11,] # typy w liście to string
# #
# # for i in lista2:
# #     lista_z.append(str(i))
# #
# # for elem in lista_z:
# #     '''
# #     sam w sobie element to zapis z tablicy ASCII
# #     01 a == A
# #     a == a
# #         wykonaj :)
# #     '''
# #     try:
# #         int(elem)
# #         lista_int.append(elem)
# #     except:
# #         if elem == elem.upper():
# #             listaduze.append(elem)
# #         if elem == elem.lower():
# #             listamale.append(elem)
# #         else:
# #             listarozne.append(elem)
# #
# # # print(''.join(lista_z))
# # # print(lista_int)
# # # print(listaduze)
# # # print(listamale)
# # # print(listarozne)
# #
# # dodaj = []
# # for elem in lista_int:
# #     dodaj.append(int(elem))
# #
# # print(dodaj)
# # print(sum(dodaj))
# #
# # def func_two_lastone(x):
# #     z = []
# #     z.append(x.pop())
# #     z.append(x.pop())
# #     return print(sum(z))
# #
# # func_two_lastone(dodaj)
# #
# #
# # '''
# # ZADANIE DOMOWE
# #
# # 1. Napisz 3 funkcje wykorzystujące pętle for i listy (w dowolny sposób).
# #
# # 2. Napisz 3 funkcje wyciągające ostatnie elementy z różnych list i sumujące je ze sobą, lub dodające, lub mnożące (dwie różne listy wystarczą)
# #
# # 3. Dodaj do kalkulatora "Historię działań (samych ich nazw)" magazynowanych w listach :) z możliwością wyświetlenia
# #     po wpisaniu komendy liczbowej lub słownej (dowolnie wybór).
# #
# # 4. Spróbuj pobawić się try i except tak jak w powyższym kodzie (pamiętaj o strukturze)
# #     try:
# #         coś co jest poddane w próbę
# #         coś co dzieje się po zdanym teście powyżej :)
# #     except:
# #         coś co dzieje się w przypadku niezdanego testu :)
# #         (może być pass)
# #
# # '''
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