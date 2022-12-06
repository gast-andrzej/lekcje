'''
1. Napisz funkcje która stworzy mi liste liczb od 1 do 100

1.1 *użyj list comprehension

2. Napisz funkcje która zwróci mi listę kwadratów elementów od 1 do 100

2.1 *użyj list comprehension

3. Napisz mi funkcje która zwróci listę kwadratów elementów parzystych od 1 do 100

4. Napisz mi funkcje która zwróci listę kwadratów elementów nieparzystych

5. Napisz mi funkcje która zwróci listę ujemnych kwadratów elementów nieparzystych
'''


#
# def func1():
#     c = list(range(1,101))
#     b = []
#     for i in c:
#         j = i*i
#         b.append(j)
#     print(b)
#
# func1()
#

'''
napisz funkcje która zwróci mi listę z liczbami parzystymi używając list comprehension w zakresie do 100

masz na to 3 linijki kodu
'''
#
# def func():
#     '''comprehension'''
#     print(nasza lista)



'''
REKURENCJA

Wywołanie funkcji wewnątrz innej funkcji

'''
'''
def func1():
    c = list(range(2,101,2))
    return c

def func2():
    b = func1()
    z = []
    for i in b:
        j = i*i*i
        z.append(j)
    return z

def func3():
    g = []
    z = func2()
    for i in z:
        if i%16 == 0:
            g.append(i)
        else:
            pass
    print(g)

func3()
'''

'''
Napisz funkcje rekurencyjną przetwarzającą elementy z func1 celem sprawdzenia czy są parzyste czy nie

def _func1():
    c = []
    for i in range(0,1000):
        c.append(i)
    return c

Napisz funkcje nr 3 która podniesie wszystkie liczby parzyste z naszej func2 do potęgi 3 ale wewnątrz zwracanej listy 
będą elementy nieparzyste niepodniesione do żadnej potęgi.

'''
#
# def func1():
#     c = list(range(1,101))
#     return c
#
# def func2():
#     c = func1()
#     d = []
#     for i in c:
#         if i % 2 == 0:
#             d.append(i)
#         else:
#             d.append(i)
#     return d
#
# def func3():
#     c = func2()
#     d = []
#     for i in c:
#         if i % 2 == 0:
#             j = i*i*i
#             d.append(j)
#         else:
#             j = i
#             d.append(j)
#     return d
#
# '''
# Napisz funkcje przyjmującą func3 ale elementy nieparzyste mają być ujemną wartością potęgowania ich do potęgi 3
# '''
#
# def func4():
#     c = func3()
#     d = []
#     for i in c:
#         if i % 2 == 1:
#             j = i * i * (-i)
#             d.append(j)
#         else:
#             d.append(i)
#     print(d)
#
# func4()


'''
praca domowa REKURENCJA

**PRACA DOMOWA napisz funkcje zwracającą sumę elementów z funkcji (func4)

1. napisz funkcje zwracającą listę od 1 do 100

* w list comprehension

2. napisz funkcje przyjmującą  elementy parzyste z listy przygotowanej przez func1 i mnożące je razy 2

3. Napisz funkcje przyjmującą elementy nieparzyste z listy przygotowanej przez func1 i mnożące je razy 2

4. Napisz funkcje sprawdzającą sumę elementów z równania (funkcja 2(jej lista) - funkcja 3(jej lista)) (z ich elementów list)

5. powiedzieć czy suma z funkcji 4 jest ujemna czy dodatnia i czy jest parzysta czy nie i czy jest podzielna przez 7 używając
   stringów funkcyjnych :)
'''
