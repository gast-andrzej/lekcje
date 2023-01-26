# class Osoba:
#     def __init__(self, imie, nazwisko, rok_urodzenia):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.rok_urodzenia = rok_urodzenia
#
#     def przedstaw_sie(self):
#         return print(f"Cześć nazywam się {self.imie} {self.nazwisko}")
#     def urodziny(self):
#         return print(f"Urodziłem się {self.rok_urodzenia}")
#
#
# if __name__ == "__main__":
#     Jan = Osoba("Jan", "kowalski", "19.01.1998")
#     Jan.przedstaw_sie()
#     Jan.urodziny()




'''

Co odróżnia obiekt od klasy

słowo class

Tworzenie obiektów i wyciąganie z nich najpotrzebniejszych funkcji

działanie na elementach abstrakcyjnych

'''
import string

'''
Co posiada każdy człowiek?

Klasą określamy pojęcie     Osoba     klasę definiujemy przez słowo kluczowe class
Imie
Nazwisko
Płeć
Zawód
Tel
Email

Obiekt to fizyczna instancja klasy

Przedszkolak -> Osoba



???
Zosia

Tomek

Adrian

Kajetan

Ania



'''
#
# class Osoba:
#     def numer_tel(self):
#         print(self.Telefon)
#
#     def email_podaj(self):
#         print(self.Email)
#
#     def __init__(self, Imie, Nazwisko, Plec, Wiek, Telefon, Email):
#         self.Imie = Imie
#         self.Nazwisko = Nazwisko
#         self.Plec = Plec
#         self.Telefon = Telefon
#         self.Email = Email
#         self.Wiek = Wiek
#
#
#
# Jan = Osoba("Jan", "Kowalski", "Chłopiec", 9, 888777998, "coscos@coscoscos.cos")
# Adam = Osoba("Adam", "Nowak", "Chłopiec", 8, 884557998, "coscos123@coscoscos.cos")
#
#
#


class Auto:
    def rok_p(self):
        return self.rok
    def marka(self):
        return print(self.marka)
    def przebieg_p(self):
        return self.przebieg

    def przeglad(self):
        b = []
        b.append(self.marka)
        b.append(self.rok)
        b.append(self.przebieg)
        return b

    def __init__(self, marka, rok, przebieg):
        self.marka = marka
        self.rok = rok
        self.przebieg = przebieg


BMW = Auto("BMW", 1997, -1000)
AUDI = Auto("Audi", 1998, -2000)
MATIZ = Auto("Matiz", 1996, -5000)





#
#
# def raport_dobowy():
#     z = []
#     z.append(AUDI.przeglad())
#     z.append(BMW.przeglad())
#     z.append(MATIZ.przeglad())
#     return z
#
# def func1():
#     b = []
#     b.append(raport_dobowy())
#     b.append(raport_dobowy())
#     p1 = b[0]
#     p2 = b[1]
#     auto1 = p1[1]
#     auto2 = p2[2]
#     przebieg1 = auto1[2]
#     przebieg2 = auto2[2]
#     if przebieg1 > przebieg2:
#         print(auto2)
#     else:
#         print(auto1)
#
# func1()
#
#
#
#
#



def func1():
    return list(string.ascii_letters)

# func1()

def func2():
    return print(dict(zip(list(range(0,100)),list(string.ascii_letters))))

# func2()

def func3():
    return list(range(0,101,2))


# func3()

def func4():
    return list(range(1,101,2))

# func4()

def func5():
    return print(sum(func3())-sum(func4()))

# func5()

def func6():
    return print(sum(list(range(0,101,2)))-sum(list(range(1,101, 2))))

func6()

































