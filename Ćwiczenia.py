# '''
#
# 1. Utwórz listę liczb całkowitych i napisz funkcje (i dodaj do niej prosty interfejs konsolowy) wykonującą następujące operacje:
#
#     -Wydrukuj wartości minimalne i maksymalne
#     -Wydrukuj sumę wszystkich liczb
#     -Wydrukuj średnią z liczb
#
# 2. Utwórz program, który pobiera listę słów
#     i zwraca słowa, które mają dokładnie cztery litery.
#
# 3. Napisz funkcję, która pobiera listę napisów i zwraca
#     nową listę ze wszystkimi napisami zamienionymi na wielkie litery.
#
# 4. Mając listę liczb, napisz funkcję, która zwraca drugą co do wielkości liczbę.
#
# 5. Utwórz funkcję, która przyjmuje dwie listy i
#     zwraca wartość True, jeśli mają one co najmniej jednego wspólnego członka.
#
# 6. Mając listę liczb, napisz funkcję usuwającą z listy wszystkie liczby parzyste.
#
# 7. Napisz program w Pythonie, który znajdzie najdłuższe słowo na liście słów.
#
# 8. Napisz program w Pythonie, który znajdzie najczęściej występujący element na liście.
#
# 9. Utwórz program, który przyjmuje zdanie (łańcuch znaków) i oblicza liczbę liter i cyfr.
#
# 10. Napisz program w Pythonie, który znajdzie drugą najmniejszą liczbę na liście.
#
# 11. Utwórz program, który odczytuje plik CSV i drukuje sumę wszystkich wartości w określonej kolumnie.
#
# 12. Napisz program w Pythonie usuwający duplikaty z listy.
#
# 13. Utwórz program, który pobiera listę liczb i zwraca największą liczbę pierwszą na liście.
#
# 14. Napisz program w Pythonie, aby znaleźć wspólne elementy między dwiema listami.
#
# 15. Utwórz program, który akceptuje sekwencję liczb oddzielonych przecinkami i generuje listę oraz krotkę z tymi liczbami.
#
# 16. Napisz program w Pythonie, aby uzyskać różnicę między dwiema listami.
#
# 17. Mając listę ciągów, napisz funkcję usuwającą wszystkie samogłoski z każdego ciągu na liście.
#
# 18. Utwórz program, który wczytuje plik CSV i konwertuje dane do słownika Pythona.
#
# 19. Napisz program w języku Python, który będzie obsługiwał wyjątki podczas
#      próby konwersji ciągu znaków na liczbę całkowitą. Jeśli łańcuch nie jest
#      prawidłową liczbą całkowitą, wyświetl komunikat „Nieprawidłowe dane wejściowe”.
#
# 20. Biorąc pod uwagę listę liczb, utwórz nową listę zawierającą
#         wszystkie liczby z podanej listy, które są dodatnie.
#
# Biorąc pod uwagę tablicę liczb całkowitych, znajdź maksymalne i minimalne elementy w tablicy.
#
# Biorąc pod uwagę listę liczb, znajdź drugą co do wielkości liczbę na liście.
#
# Biorąc pod uwagę listę słów, znajdź słowo, które pojawia się najczęściej na liście.
#
# Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.
#
# Napisz funkcję generującą n pierwszych liczb pierwszych.
#
# Napisz funkcję, która pobiera łańcuch jako dane wejściowe i zwraca odwrotność ciągu.
#
# Mając listę liczb, napisz funkcję, która znajdzie średnią liczb.
#
# Napisz funkcję, która pobiera listę liczb i zwraca drugą najmniejszą liczbę na liście.
#
# Napisz funkcję sortującą listę liczb w porządku rosnącym.
#
# Napisz funkcję sprawdzającą, czy podany ciąg znaków jest palindromem.
#
# Napisz funkcję sprawdzającą, czy dwa łańcuchy są swoimi anagramami.
#
# Napisz funkcję generującą wszystkie możliwe permutacje podanego ciągu znaków.
#
# Napisz funkcję implementującą algorytm wyszukiwania binarnego.
#
# Napisz funkcję sprawdzającą, czy podana liczba jest liczbą Fibonacciego.
#
# Napisz funkcję generującą pierwsze n liczb Fibonacciego.
#
# Napisz funkcję, która znajdzie największy wspólny dzielnik dwóch liczb.
#
# Napisz funkcję implementującą algorytm sortowania przez scalanie.
#
# Napisz funkcję, która znajdzie najdłuższy rosnący podciąg w podanej tablicy liczb.
#
# Napisz funkcję, która znajdzie najkrótszą ścieżkę między dwoma wierzchołkami grafu.
#
# Napisz funkcję sprawdzającą, czy dany graf jest drzewem.
#
# '''
# import random
# import statistics
#
# c = [47, 61, 39, 27, 27, 50, 23, 77, 47, 47, 8, 37, 15, 26, 54, 71, 62, 48, 98, 14]
# c1 = [55,66,77,88,99,4,6,3,3,6,3,77]
# c2 = [111,112,113,543,467,335]
# x = ["alba", "kot", "tomasz", "samochody", "car", "kolo", "CDRV", "hello", "Opel", "Vole", "Volvo"]
# x1 = ["baba", "kot", "katze"]
# x2 = ["pies", "krowa", "baran"]
#
# def func1(x):
#     z = 0
#     b = 0
#     while True:
#         indexer = int(input(" menu "))
#         match indexer:
#             case 1:
#                 print(min(x))
#                 print(max(x))
#             case 2:
#                 print(sum(x))
#                 # for i in x:
#                 #     z = z + i
#                 # print(z)
#                 # z = 0
#             case 3:
#                 print(statistics.mean(x))
#                 # for i in x:
#                 #     z = z + i
#                 #     b += 1
#                 # sr = z/b
#                 # print(sr)
#             case 4:
#                 break
#
# # func1(c)
#
# def func2(x):
#     for i in x:
#         z = len(i)
#         if z == 4:
#             print(i)
#         else:
#             pass
# # func2(x)
#
#
# def func3(x):
#     g = []
#     for i in x:
#         g.append(''.join(i.upper()))
#     return print(g)
# func3(x)
#
# def func4(c):
#     c.sort()
#     c.reverse()
#     print(c[1])
#
# # func4(c)
#
# def func5(x,y):
#     for i in x:
#         if i not in y:
#             g = False
#             print(g)
#         else:
#             g = True
#             print(g)
#
# # func5(x2, x)
#
#
# def func6(numbers):
#     return print([num for num in numbers if num % 2 != 0])
#
# # func6(c)
#
# # def func7(x):
# #     bb = []
# #     for i in x:
# #         g = len(i)
# #         bb.append(g)
# #         h = int(max(bb))
# #     for i in x:
# #         if len(i) == int(h):
# #             print(i)
#
#
# # func7(x)
# import collections
#
# bx = 'ala ma kota'
#
# def func8(x):
#     cout = collections.Counter(x)
#     print(cout.most_common(1)[0][0])
#
# # func8(c)
#
# def func9(x):
#     print(len(x))
#
# # func9(bx)
#
# def fibon(x):
#     for i in range(0,x):
#         print(i**i)
# # fibon(10)
#
#
#
#
# def fibona(n):
#     b = []
#     g = []
#     for i in range(0,n):
#         b.append(i)
#     for i in (2, len(b)-1):
#         z = b[i-1] + b[i-2]
#         g.append(z)
#         z = 0
#
# # fibona(100)
#
import collections

cvs = [47, 61, 39, 27, 27, 50, 23, 77, 47, 47, 8, 37, 15, 26, 54, 71, 62, 48, 98, 14]
xvs = ["alba", "kot", "tomasz","tomasz","tomasz", "samochody", "car", "kolo", "CDRV", "hello", "Opel", "Vole", "Volvo", "Volvo"]
#
# def func21(x):
#     z = set()
#     for i in x:
#         z.add(i)
#     c = []
#     for i in z:
#         c.append(i)
#     # c.sort()
#     # c.reverse()
#     print(c)
# # func21(xvs)
#
#
# #
# #
# #
# # def funcg(x):
# #     ff = []
# #     indexlist = []
# #     for i in x:
# #         print(i.)
# # funcg(x)
# #
# #
# #

# def func8(x):
#     cout = collections.Counter(x)
#     print(cout.most_common(1)[0][0])
#
# func8(xvs)


def func1(x):
    gg = []
    for i in x:
        gg.append(len(i))
    print(gg)

# func1(xvs)











# dane user

# hasło

# email

def tupler():
    kk = []
    for i in range(0,3):
        in1 = input()
        kk.append(in1)
    return tuple(kk)


def func2():
    tupel = tupler()
    bb = []
    for i in tupel:
        g = i
        bb.append(g)
    return bb



def func3():
    gg = func2()
    f = set()
    listag = []
    for i in gg:
        f.add(i)
    if len(f) == 3:
        listag.append(f)
        listag.append(True)
        return listag
    else:
        listag.append(False)
        return listag


def func4():
    boolex = func3()
    boolex2 = boolex.pop()
    if boolex2 == True:
        b = open("usery.txt", "a")
        b.write(f"{boolex[0]}\n")
    else:
        print("sorry")

# func4()



def func2222():
    lista = [10,5,7,8,9,0]
    return print(lista[0])

func2222()
