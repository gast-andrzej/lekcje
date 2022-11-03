# x = int(input("Wprowadź liczbę: "))
#
# def func1(x):
#     return print(f"Jeżeli do {x} dodasz 65 to wynikiem takiego działania będzie {x + 65}")
#
# def func2(x):
#     return print(f"Jeżeli od {x} odejmiesz 19 to wynikiem takiego działania będzie {x - 19}")
#
# def func3(x):
#     return print(f"Jeżeli  {x} pomnożysz z 49 to wynikiem takiego działania będzie {x * 49}")
#
# def func4(x):
#     return print(f"Jeżeli {x} podzielisz przez 5 to wynikiem takiego działania będzie {x / 5}")
#
# def func5(x):
#     return print(f"Jeżeli {x} podzielisz przez 3 to wynikiem takiego działania będzie {x % 3}")
#
# def func6(x):
#     return print(f"{x} procent z 241 to {(241/100)*x}")

# instrukcja warunkowa
'''
jeżeli COŚ:
    to zrób coś
jeżeli coś innego:
    to zrób coś innego
w każdym innym przypadku:
    zrób to, lub nic

if x%2 == 0 or x == 3:
    hello
elif x%3 != 0:
    not hello
else:
    bye

wartości logiczne pochodzą z logiki Boole'a

True
False

domyślna wartość instrukcji warunkowej to True

operatory logiczne 

== jest równe

!= nie jest równe

and operator i 

or operator lub

'''

x = 15

def funcinstr(x):
    if x%3 == 0 or x == 15:
        print("Hello")
    elif x == 16:
        print("ok")
    else:
        print("Not today")

funcinstr(x)


# niech dana funkcja sprawdza czy wpisana liczba jest parzysta czy nie


'''
10
dzielenie podzieli te 10 na 2 


modulo 
10 -2 -2 -2 -2 -2 ???? czy jeszcze mogę zabrać 2?

jak nie to wypisze co jest na końcu takiego 



'''
def dodawanie():
    x=int(input())
    y=int(input())
    return print(x+y)


def odejmowanie():
    x=int(input())
    y=int(input())
    return print(x-y)

def func1():
    while True:
        index = input()
        if index.upper() == "DODAWANIE":
            dodawanie()
        elif index.upper() == "ODEJMOWANIE":
            odejmowanie()
        elif index.upper() == "EXIT":
            break


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