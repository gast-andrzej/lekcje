'''
OBIEKTÓWKA =D

co to class
co to obiekt
czym jest słówko __init__
Co to funkcje prywatne
Co to funkcje statyczne
Deklaracja zmiennych w obiekcie
Deklaracja wykonania funkcji w obiekcie


Czym jest dziedziczenie
Co się dziedziczy
Czym jest super init




'''
import string

'''
import string




class obiekt:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class obiekt2(obiekt):
    def __init__(self, x = None, y = None):
        super().__init__(x, y)
        self.x = x
        self.y = y
        y = []
        x = []
        for i in string.ascii_letters:
            y.append(i)
        for i in range(0, int(len(y))):
            x.append(i)
        dicter = dict(zip(x,y))
        print(dicter)


obiekt2()

'''


# turtel :D
#
# import turtle
#
#
#
# def func1():
#     for i in range(0,30):
#         turtle.color("red", "yellow")
#         turtle.begin_fill()
#         turtle.forward(50)
#         turtle.left(50)
#         turtle.left(50)
#         turtle.left(50)
#         turtle.color("white")
#
#
# def func2():
#     z = random.randint(-200,200)
#     y = random.randint(-200,200)
#     turtle.goto(z,y)
#
# def func3():
#     for i in range(0,10):
#         func1()
#         func2()
#
#
# func3()

'''
MAGIC WORDS (Magic Methods)

__init__

__add__ 

__sub__

__mul__

__divmod__

__truediv__

__floordiv__

__mod__

__new__

__str__

__ne__

__le__

__ge__

__eq__

__it__

__pow__()

__sizeof__()

'''

'''
MAGIC WORDS (Magic Methods)

__init__ = inicjacja obiektu

__add__ = dodawanie 

__new__ = nowy obiekt

__str__ = zamiana w str

__ge__ - operator >= logika bool

__pow__() - podniesienie do potęgi

__sizeof__(self) - ile element zajmuje w bitach

'''


'''
Dynamiczne - program jest w postaci venv (wirtualne środowisko) które wykonuje się z góry na dół, bez konieczności
            ciała programu

Kompilowalne - tworzy się program (obiekt) i dopiero on zaczyna działać w ustalonej wewnętrznie strukturze
                (taką strukturą w tym programie są funkcje statyczne - odpowiedzialne za działanie programu)
'''



class Obiekt:
    '''
    Co takiego posiada obiekt?

    Obiekt posiada siebie czyli tzw.(self)

    Obiekt może posiadać parametry

    Obiekt może posiadać funkcje strzeżone jak _func1 _func2

    Obiekt posiada jeszcze funkcje inicjującą jego działanie __init__

    '''


    def _func1(self, b):
        self.b = b
        print(b)
        lista = list(range(0,100))
        return lista

    def _func2(self=None):
        z = list(string.ascii_letters)
        return z

    def __init__(self):
        v = input("wprowadź liczbę ")
        dictionaries = dict(zip(Obiekt._func1(self, v), Obiekt._func2()))
        print(dictionaries)


class Samochod:

    def func1(self=None):
        x = input()
        y = input()


    def __init__(self):
        Samochod.func1()



class kalkulator:

    def _dodawanie(self=None):
        x = int(input("pierwsza liczba "))
        y = int(input("druga liczba "))
        z = x+y
        return z




    def __init__(self):
        indexer = int(input("jakie działanie chcesz zrobić? \n"
                            "1 dodawanie\n"
                            "2 odejmowanie\n"
                            "3 mnożenie\n"
                            "4 dzielenie\n"
                            "5 potęgowanie\n"
                            "6 sprawdzenie czy liczba jest parzysta\n"
                            "7 sprawdzenie pierwiastka z danej liczby\n"
                            "8 podniesienie kwadratowe liczby\n"
                            "9 dzielenie z resztą\n"
                            ""))

        '''
        spraw by kalkulator był odporny na zepsucie (użyj try)
        '''

        if indexer == 1:
            print(kalkulator._dodawanie())


kalkulator()