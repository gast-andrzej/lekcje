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
