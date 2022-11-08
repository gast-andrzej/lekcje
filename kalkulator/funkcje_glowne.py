from funkcje_skladowe import dodawanie
from funkcje_skladowe import odejmowanie
from funkcje_skladowe import mnozenie
from funkcje_skladowe import dzielenie





def kalkulator_exe():
    matcher = 9
    while matcher >= 0:
        x = int(input("pierwsza liczba "))
        y = int(input("druga liczba "))
        index = int(input("1 dodawanie, 2 odejmowanie, 3 mnożenie, 4 dzielenie, other value = exit"))
        # to tutaj jest encoding CP1250 lub latin2, natomiast nie UTF-8, jak już UTF-16
        pytajnik = str(input("You want that? [Y][N]"))
        if pytajnik.upper() == "Y":
            if index == 1:
                dodawanie(x, y)
                #tutaj np. miejsce na historie :) w tej linijce
                matcher = matcher - 1
            elif index == 2:
                odejmowanie(x, y)
                matcher = matcher - 1
            elif index == 3:
                mnozenie(x, y)
                matcher = matcher - 1
            elif index == 4:
                dzielenie(x, y)
                matcher = matcher - 1
            else:
                break
        else:
            pass