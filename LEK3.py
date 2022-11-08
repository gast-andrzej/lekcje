'''
Listy, tuple, pętla for, zakresy
'''

'''
Praca Domowa
'''

'''
1
napisz kolejne funkcje dla kalkulatora w tym funkcje procent i liczenie obwodu prostokąta i kwadratu

2
Użytkownik ma mieć możliwość wyboru tylko 10 razy danej funkcji kalkulatora, później ten automatycznie
się zamyka, oczywiście wcześniej sam może go zamknąć

3
użytkownik ma możliwość wpisania polecenia do kalkulatora co chce zrobić i kalkulator zapyta go czy na pewno
chce to zrobić nim podejmie działanie :)

'''
'''
def dodawanie(x,y):
    return print(x+y)

def odejmowanie(x,y):
    return print(x-y)

def mnozenie(x,y):
    return print(x*y)

def dzielenie(x,y):
    return print(x/y)




def kalkulator():
    matcher = 9
    while matcher >= 0:
        x = int(input("pierwsza liczba "))
        y = int(input("druga liczba "))
        index = int(input("1 dodawanie, 2 odejmowanie, 3 mnożenie, 4 dzielenie, other value = exit"))
                # to tutaj jest encoding CP1250 lub latin2, natomiast nie UTF-8, jak już UTF-16
        pytajnik = str(input("You want that? [Y][N]"))
        if pytajnik.upper() == "Y":
            if index == 1:
                dodawanie(x,y)
                matcher = matcher - 1
            elif index == 2:
                odejmowanie(x,y)
                matcher = matcher - 1
            elif index == 3:
                mnozenie(x,y)
                matcher = matcher - 1
            elif index == 4:
                dzielenie(x,y)
                matcher = matcher - 1
            else:
                break
        else:
            pass

kalkulator()

'''

def dodawanie(x,y):
    return print(x+y)

def odejmowanie(x,y):
    return print(x-y)

def mnozenie(x,y):
    return print(x*y)

def dzielenie(x,y):
    return print(x/y)




def kalkulator():
    matcher = 9
    while matcher >= 0:
        x = int(input("pierwsza liczba "))
        y = int(input("druga liczba "))
        index = int(input("1 dodawanie, 2 odejmowanie, 3 mnożenie, 4 dzielenie, other value = exit"))
                # to tutaj jest encoding CP1250 lub latin2, natomiast nie UTF-8, jak już UTF-16
        pytajnik = str(input("You want that? [Y][N]"))
        if pytajnik.upper() == "Y":
            if index == 1:
                dodawanie(x,y)
                matcher = matcher - 1
            elif index == 2:
                odejmowanie(x,y)
                matcher = matcher - 1
            elif index == 3:
                mnozenie(x,y)
                matcher = matcher - 1
            elif index == 4:
                dzielenie(x,y)
                matcher = matcher - 1
            else:
                break
        else:
            pass

kalkulator()




