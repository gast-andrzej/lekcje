# '''
#
# zagadnienie FIFO i kolejka, czym się różni od stosu  VIP user LIFO
#
# dzisiaj listy przyjmują dane wprowadzone przez usera
#
# kolejny element to nadawanie numeru zamówienia wg wytycznych w liście
#
# ostatni element to przekazanie zamówień do listy końcowej
#
# tworzymy liste z wyrzuceniem pierwszych elementów (kolejka)
#
# następnie tworzymy listę zagnieżdżoną działającą jak kolejka
#
#
#
#
# KOLEJKA
#
#
# import queue
#
# b = queue.Queue()
# b.put(1)
# b.put(10)
# b.put(2)
# b.put(3)
# print(b.get())
# print(b.get())
# print(b.get())
# print(b.get())
#
#
# STOS
#
#
# t1 = [1,2,3,4,5,6,7]
#
# print(t1.pop())
# print(t1.pop())
# print(t1.pop())
# print(t1.pop())
# print(t1.pop())
# print(t1.pop())
# print(t1.pop())
#
#
#
# '''
#
#
#
#
#
# '''
# FIFO --> First in first out
#
#
# FILO --> First in last out
#
#
# LIFO --> Last in First out ---> jest zastosowaniem dla klientów VIP
#
# '''
#
# import random
#
# def func_przygotowanie():
#     zamowienie = []
#
#     numerzamowienia = random.randint(1000,5000)
#     numerklienta = random.randint(0,5)
#     karta = int(random.randint(0,1)) # 1 char P - zwykły user, V - to jest VIP
#
#
#     for i in range(0,1):
#         karta = int(random.randint(0, 1))
#         match karta:
#             case 0:
#                 karta = "P"
#             case 1:
#                 karta = "V"
#
#         zamowienie.append(numerzamowienia)
#         zamowienie.append(numerklienta)
#         zamowienie.append(karta)
#
#     return zamowienie
#
# def func_lista_all():
#     lista_zamowien = []
#     for i in range(0,200):
#         lista_zamowien.append(func_przygotowanie())
#     return lista_zamowien
#
# def sortowanie():
#     zamowienia = []
#     vipy = []
#     persons = []
#     b = func_lista_all()
#     for i in b:
#         index = i[2]
#         match index:
#             case "P":
#                 persons.append(i)
#             case "V":
#                 vipy.append(i)
#     print(vipy)
#     print('')
#     print('')
#
#     print(persons)
#     print('')
#     print('')
#     print('')
#
#
#     user0 = 0
#     user1 = 0
#     user2 = 0
#     user3 = 0
#     user4 = 0
#     user5 = 0
#
#     for i in vipy:
#         indexer = i[1]
#         match indexer:
#             case 0:
#                 user0 += 1
#             case 1:
#                 user1 += 1
#             case 2:
#                 user2 += 1
#             case 3:
#                 user3 += 1
#             case 4:
#                 user4 += 1
#             case 5:
#                 user5 += 1
#     zamowienia.append(f"user0 zamówił {user0} rzeczy")
#     zamowienia.append(f"user1 zamówił {user1} rzeczy")
#     zamowienia.append(f"user2 zamówił {user2} rzeczy")
#     zamowienia.append(f"user3 zamówił {user3} rzeczy")
#     zamowienia.append(f"user4 zamówił {user4} rzeczy")
#     zamowienia.append(f"user5 zamówił {user5} rzeczy")
#
#     sumazamowienvip = user0+user1+user2+user3+user4+user5
#
#     print(zamowienia)
#     print(sumazamowienvip)
#
#
#     return vipy, persons
#
# sortowanie()
# #
# # def funkcjarzut(n):
# #     # prawdopodobieństwo wypadnięcia kolejnego wyniku
# #     orzel = 0
# #     reszka = 0
# #     for i in range(0,n):
# #         b = random.randint(0, 1)
# #         match b:
# #             case 0:
# #                 print("orzeł")
# #                 orzel += 1
# #             case 1:
# #                 print("reszka")
# #                 reszka += 1
# #     if (orzel/n) >= (reszka/n):
# #         print("orzeł powinien być następnym wynikiem")
# #     else:
# #         print("reszka powinna być następnym wynikiem")
# #     b = random.randint(0, 1)
# #     match b:
# #         case 0:
# #             print("orzeł")
# #             orzel += 1
# #         case 1:
# #             print("reszka")
# #             reszka += 1
# #
# # funkcjarzut(50)
# import random

#
# def func1():
#     lista = []
#     baker = (random.randint(0,100),
#              random.randint(0,100),
#              random.randint(0,100),
#              random.randint(0,100),
#              random.randint(0,100),)
#     lista.append(baker)
#     print(lista)
#     print(lista[0])
#
# func1()


'''
ZADANKA :)
    - zsumuj elementy z list (tylko int z list wewnątrz t1 do wspólnej wartości)

    t1 = [[1,2,3,"OOP",65,32],[23,43,"Comming",22,11,13,"G"],["T","KALMAR","B","O",8,"I",3,"JK"],["Soon", 5,1]]

'''
'''
value b = 0

wyciągnięcie list z listy
for

wyciągnąć elementy z list wyciągniętych
for

sprowadzenie do int wartości z wyciągniętych list
try

wyświetl sumę (b)

'''


'''
PRZEĆWICZENIE PRACA DOMOWA

Napisz i zaprojektuj funkcje dodającą elementy do listy i wyświetlającą jej elementy
Napisz i zaprojektuj funkcje wyrzucającą od ostatniego elementu z listy i wyświetlającą te elementy
Napisz i zaprojektuj funkcje dodającą nowe listy do listy
Napisz i zaprojektuj funkcje wyrzucającą ostatni element z listy który jest listą (z listy t1) (jest ono na 8 znaków i 1 linijke)
Napisz funkcje sumującą wszystkie integery w liście
podrasuj istniejące funkcje o wyrzucanie wyjątku ValueError
podrasuj istniejące funkcje o zliczanie wyrzuconych wyjątków ValueError



'''

