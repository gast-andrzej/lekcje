'''
Cz.1
Pełniak listy, funkcje, pętle, zmienne, random, math, wyjątki, instrukcje warunkowe,

TUPLA -> To taka Consta (element stały i niezmienny) wśród LIST i na tym polega jej niemutowalność ! :)

Cz.2
struktura mastermind i pisanie masterminda

*Cz.2.1
pierwszy automat (Moor'a)

Cz.3
Wstęp do OOP
'''


# tupla = (1, "Hello", "Z", "AlbA", 7, 43, "World", 2, 0)


'''
Napisz funkcje która przyporządkuje elementy tupli do listy bądź setu.
'''
#
# def func1(x):
#     lista1 = []
#     set1 = []
#     for i in x:
#         # try:
#         #     int(i)
#         #     set1.append(i)
#         # except:
#         #     lista1.append(i)
#         '''
#         Instrukcja warunkowa
#         '''
#     print(lista1)
#     print(set1)
#
# func1(tupla)
#
#
#
# tupla2 = (5,3,2,6,8,"HELLO","kali",12,8,7,55,123, "maciek",5, "WORLD","x")
#
# '''
# Napisz funkcje która rozdzieli stringi od integerów do poszczególnych list i setów
# '''
#
# def func1(x):
#     lista_male = []
#     lista_duze = []
#     set_parzyste = []
#     set_nieparzyste = []
#
#     for i in x:
#         try:
#             int(i)
#             if i%2 == 0:
#                 set_parzyste.append(i)
#             else:
#                 set_nieparzyste.append(i)
#         except:
#             if i == i.upper():
#                 lista_duze.append(i)
#             else:
#                 lista_male.append(i)
#     print(lista_male)
#     print(lista_duze)
#     print(set_nieparzyste)
#     print(set_parzyste)
#
# func1(tupla2)
#












#
# tupla3 = (8,"!",7,4.4,15,"Hello",2.2,7.7,77.6,"World",77.7,"Loki",8)
#
#
#
# def func1(x):
#     lista1 = []
#     set1 = []
#     set_float = []
#     b = 0
#     # b = wartość
#
#     for i in x:
#         try:
#             int(i) or float(i)
#             if type(i) == float:
#                 set_float.append(i)
#             else:
#                 set1.append(i)
#         except:
#             lista1.append(i)
#
#     for i in set1:
#         b = b+i
#
#
#     print(set1)
#     print(set_float)
#     print(lista1)
#     print(b)
#
#
#
# func1(tupla3)

import random
import string

def func1():
    intlista = []
    strlist = []
    listatup = []
    indexer = 0

    for i in string.ascii_letters:
        strlist.append(i)
    for i in range(0,30):
        intlista.append(random.randint(0,1000))

    for i in range(0,120):
        indexer = random.randint(0,1)
        if indexer == 1:
            listatup.append(strlist[random.randint(0,len(strlist)-1)])
        else:
            listatup.append(intlista[random.randint(0,len(intlista)-1)])
    print(listatup)


func1()














'''
tupla1 = (750, 'J', 750, 476, 618, 'a', 'o', 530, 'V', 'u', 903, 'G', 'K', 425, 717, 25, 10, 'm', 61, 'A', 476, 'Y', 618, 903, 'N', 'L', 'l', 'c', 618, 'i', 'J', 901, 582, 37, 425, 'j', 436, 476, 'V', 231, 195, 'x', 338, 61, 'f', 231, 866, 'N', 'l', 860, 37, 717, 'g', 866, 'i', 'R', 'f', 425, 'P', 984, 'R', 'b', 618, 'v', 'W', 860, 'P', 618, 'D', 251, 'X', 'x', 693, 476, 530, 'S', 10, 860, 693, 866, 338, 'r', 984, 'r', 231, 984, 483, 476, 'T', 'P', 984, 251, 'Q', 'a', 530, 984, 'H', 483, 'E', 901, 'R', 'Q', 'z', 25, 958, 860, 'O', 120, 'Q', 'g', 483, 't', 37, 't', 'm', 'Q', 866, 't', 615, 'a')
tupla2 = (701, 480, 29, 63, 'T', 'l', 519, 368, 221, 'p', 'N', 'x', 'M', 496, 'S', 'Q', 'p', 'H', 899, 760, 251, 719, 368, 760, 990, 701, 701, 884, 'A', 'D', 519, 467, 701, 971, 'o', 'S', 63, 971, 807, 'M', 29, 'f', 'H', 515, 467, 151, 't', 'G', 'v', 'F', 884, 'P', 'M', 'N', 'U', 763, 't', 310, 'M', 'V', 'G', 63, 'R', 899, 990, 'a', 440, 'j', 'b', 386, 467, 'q', 'W', 536, 'f', 'c', 251, 'H', 'X', 440, 467, 701, 'M', 'F', 971, 884, 221, 'M', 251, 'G', 'e', 386, 'l', 'b', 'n', 'v', 'Y', 899, 'C', 944, 'J', 'U', 386, 'p', 'M', 'Z', 583, 990, 310, 221, 'L', 930, 440, 120, 'M', 221, 'y', 467, 'u', 719)
tupla3 = ('a', 109, 'P', 638, 'E', 'i', 180, 'h', 'o', 453, 727, 180, 'o', 'Q', 'E', 'l', 727, 318, 510, 839, 424, 'H', 761, 'I', 510, 'z', 'j', 'X', 915, 'B', 424, 180, 'b', 143, 843, 'V', 318, 56, 424, 'q', 'k', 839, 'r', 424, 796, 9, 'e', 26, 180, 'x', 863, 796, 'A', 'L', 'a', 727, 143, 424, 'Q', 'e', 'S', 'S', 'k', 829, 'o', 'R', 510, 'w', 'F', 727, 'W', 863, 'C', 'e', 'S', 638, 't', 'S', 915, 'b', 'l', 'c', 843, 26, 'u', 761, 'Z', 180, 914, 727, 'z', 180, 914, 'g', 'd', 'Z', 761, 318, 577, 'o', 914, 'a', 863, 'R', 26, 638, 'Q', 'U', 839, 839, 'k', 730, 45, 488, 531, 'J', 'r', 'U', 'd', 'L')
tupla4 = (364, 'N', 'p', 243, 'z', 716, 'd', 'y', 'V', 'p', 'b', 243, 'm', 764, 'S', 949, 'd', 405, 933, 103, 211, 'z', 243, 621, 921, 'X', 'N', 292, 'L', 12, 250, 99, 'A', 'c', 949, 'g', 'T', 'd', 'f', 103, 'u', 'q', 405, 874, 250, 'W', 'P', 292, 'O', 'E', 292, 'd', 405, 'X', 756, 'u', 'I', 351, 'V', 'R', 494, 'a', 'i', 'n', 'k', 'F', 'B', 'r', 'j', 99, 874, 5, 12, 'd', 949, 921, 405, 'c', 784, 27, 943, 'r', 'I', 784, 65, 784, 243, 'k', 'y', 764, 'V', 'V', 433, 'l', 'Y', 27, 943, 'I', 12, 'w', 'J', 'G', 'I', 952, 887, 'd', 351, 'y', 'J', 952, 'e', 351, 621, 'V', 433, 's', 943, 621, 756, 433)
tupla5 = (371, 371, 437, 'L', 641, 's', 967, 'a', 205, 'X', 15, 'O', 278, 'C', 412, 'b', 78, 684, 278, 855, 781, 871, 'h', 602, 855, 299, 'K', 437, 't', 'y', 'Y', 78, 'S', 'i', 189, 684, 751, 'D', 141, 'F', 78, 'y', 'Q', 'g', 967, 'F', 'O', 'j', 371, 716, 716, 247, 'S', 781, 'Q', 15, 915, 371, 'e', 'Z', 781, 78, 'o', 15, 299, 'D', 'o', 412, 'G', 'U', 589, 'u', 'Y', 'A', 'T', 'F', 'Z', 'B', 'c', 641, 'b', 'T', 'U', 641, 'k', 190, 'U', 'q', 0, 'h', 89, 'V', 89, 103, 247, 'Q', 412, 'g', 'p', 190, 189, 'z', 'J', 'x', 't', 'r', 716, 904, 247, 684, 15, 641, 'P', 'p', 'g', 'c', 641, 103, 15, 't')
tupla6 = (249, 's', 'F', 832, 'A', 95, 'l', 384, 'M', 30, 'V', 'J', 'i', 252, 'F', 'h', 931, 112, 255, 'k', 'q', 383, 30, 835, 381, 781, 763, 503, 294, 128, 835, 249, 'Y', 381, 284, 128, 736, 'b', 't', 730, 95, 112, 381, 'n', 128, 'u', 'T', 'N', 'Y', 'F', 730, 'z', 404, 'W', 763, 736, 781, 'i', 'o', 404, 's', 95, 404, 112, 'L', 'A', 381, 255, 837, 'F', 249, 763, 'P', 'E', 'b', 522, 'e', 'i', 'Q', 294, 835, 736, 'K', 'r', 730, 404, 30, 'X', 'w', 'v', 292, 522, 896, 835, 522, 'Z', 931, 30, 835, 522, 'Z', 'T', 's', 22, 'L', 736, 736, 837, 252, 381, 931, 128, 22, 'W', 'P', 611, 'r', 736, 30, 212)
tupla7 = (750, 'J', 750, 476, 618, 'a', 'o', 530, 'V', 'u', 903, 'G', 'K', 425, 717, 25, 10, 'm', 61, 'A', 476, 'Y', 618, 903, 'N', 'L', 'l', 'c', 618, 'i', 'J', 901, 582, 37, 425, 'j', 436, 476, 'V', 231, 195, 'x', 338, 61, 'f', 231, 866, 'N', 'l', 860, 37, 717, 'g', 866, 'i', 'R', 'f', 425, 'P', 984, 'R', 'b', 618, 'v', 'W', 860, 'P', 618, 'D', 251, 'X', 'x', 693, 476, 530, 'S', 10, 860, 693, 866, 338, 'r', 984, 'r', 231, 984, 483, 476, 'T', 'P', 984, 251, 'Q', 'a', 530, 984, 'H', 483, 'E', 901, 'R', 'Q', 'z', 25, 958, 860, 'O', 120, 'Q', 'g', 483, 't', 37, 't', 'm', 'Q', 866, 't', 615, 'a')









praca domowa:
    dla każdej tupli napisać funkcje, dzielenie na 4 różne listy wg. małych liter, dużych liter, cyfr parzystych i cyfr nieparzystych.
    dla każdej listy z liczbami podać sumę wartości w środku
    dla każdej listy z liczbami posorotować je od najmniejszej do największej i od największej do najmniejszej
    dla każdej listy policzyć ilość elementów i wskazać te które mają najwięcej elementów w sobie :) 


'''