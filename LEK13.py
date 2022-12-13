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