'''
LEKCJA POWTÓRZENIOWA

Komentarz Blokowy

# Komentarz Liniowy

'''

'''
Typy Danych

Liczbowe:
int = liczby całkowite
float = liczby zmiennoprzecinkowe
consta = stała niezmienna np. liczba pi 


Słowne:
str = słowa !!!!
    f"string {funkcyjny}"
    r"czyli///// ROW - > lokalizacja pliku"
    " zwykły string "

char = pojedyńcze znaki

Listy:
lista = [] - z reguły elementy słowne ale liczby też mogą być
set = [] - elementy liczbowe, bez elementów słownych
tuple = () - listy niezmienne niemutowalne (czyli nie działa na nie pop i inne funkcje usunięcia parametrów)
Słowniki = {x:y} - macierze

Dane wprowadzone przez użytkownika:
input()

Działania
pow() potęgowanie
% - MODULO -> Zagadnienie liczb modularnych

10%2
10 rozbijam na 2+2+2+2+2

ale modulo działa tak

x%7 = 3

x = 10
x-2-2-2-2-2(-2??not) = 0


'''

'''
STRUKTURA

hard coding - brak użycia struktury funkcji w swoim kodzie 
hard coding jest dobry ale pod pewnymi warunkami
zmienne (globalne), jeżeli projektujesz prototyp (luźny potok myśli)

programowanie funkcyjne - czyli oparte o funkcje, projektowanie narzędzi wew 
    i ich dalszy użytek poprzez fixtury (dekoratory)
    jako elementy obiektów
    
Object Orienting Programming - programowanie obiektowe, przygotowanie gotowych programów
    bądź znacznych elementów programów.
    
elementy projektowe:
    pass - element odpuszczenia
    None - Nic
'''

'''
IMPORTY

pobieranie zawartości dodatkowej (bibliotek) do swojego kodu, lub plików przygotowanych przez nas wcześniej

from - z 
import - importuj
as - jako

Przykładowy import
from kalkulator import funkcje_glowne as FG

za każdym razem jak wpiszę FG. to wyświetlą mi się tamtejsze funkcje, zmienne i obiekty wew.

'''

'''
INSTRUKCJA WARUNKOWA I LOGIKA

operatory logiczne:
    >=
    <=
    ==
    !=
    and
    or
    operator XOR (modulo) -> Exclusive OR - zawsze zwróci wartość 1 lub 0  (wartosc%2 == konkret wynik) == True 
    
elementy logiki Bool'a
    True - 1
    False - 0
    
elementy instrukcji warunkowej
    if
    elif
    else
    argument
    instrukcja wykonawcza


'''

'''
Pętle

skończona i jasno określona:

NAJWAŻNIEJSZA
for i in range(zakres od np. 0 do x)


while <argument inny niż true or false>:

pętla nieskończona? 

while True:

używamy jej do działania programów a przerwać jej działanie można słowem break


'''

'''
funkcje

def nazwafunkcji(tutaj przyjmuje parametry po przecinku):
    instrukcja działania funkcji
    return wynik działania funkcji

'''

'''
działania na listach (list comprehension)

lista = []


# LISTA ZAWSZE ZACZYNA SIĘ OD elementu o numerze 0
lista = []
x = 4,5,6,7,8,11

for i in x:
    lista.append(i)

print(lista)

print(lista.pop())
# pop to wyrzucenie ostatniego elementu z listy
print(lista)

print(lista[1])
lista[1]  wyświeli nam element z numerem 1 z listy (to element drugi)

'''

'''
biblioteka random

randint - to "pseudo" - losowa liczba z zakresu

x = random.randint(0,10)

nasz x przybierze wartość jakiejś liczby z zakresu od 0 do 10


biblioteka math

po prostu matma

math.pow() - potęgowanie
math.factorial() - silnia
math.pi - liczba pi
'''
'''
WYJĄTKI

x = input()

try:
    argument logiczny do sprawdzenia np. int(x) - czy to prawda, czy jest możliwe przełożenie naszego inputu na int
    jeśli tak to możemy działać dalej
    
except ValueError:
    jeżeli błąd wartości (nie ma możliwości tego try co u góry, to wykonaj to co tu)

inne wyjątki:
    ValueError - błąd wartości np. str wprowadzony tam gdzie miał być int
    ZeroDivision - dzielenie przez zero
    EnvoimentError - Błąd środowiska w którym pracujemy (brak zainstalowanych pakietów bądź libów)
'''

'''
Zakres i długości

len(x) - określa długość elementu x 
range(0,x) - zasięg liczb od 0 do x 
list() - tworzy nam liste elementów

np.
list(range(0,5)) - utworzy nam liste [0, 1, 2, 3, 4] pięcioelementową gdzie ostatni element to 4 a pierwszy to 0 
'''
# x = list(range(1,9+1))
# y = list(range(10,100,10))
# b = dict(zip(x,y))
#
# print(b)
'''
k = list(range(0,21,2))
f = list(range(0,21))

for i in range(0,len(f)):
    if i % 2 == 0:
        f.remove(i)
    else:
        pass


print(k)
print(f)
'''


# zadanka

'''
napisz funkcje przyjmującą dane wprowadzone przez użytkownika, funkcja ma zapisywać w sobie dane wprowadzone przez użytkownika
i je wyświetlać
'''
#
# def func1(x, y):
#     y.append(x)
#     return print(y)
#
# def func_while():
#     glist = []
#     index = 9
#     while index>=0:
#         x = input("hello")
#         func1(x, glist)
#         index = index -1





'''
Palindromy
'''

# lista = ["sos", "nos", "kajak", "rybak"]
#
# def palindrome(lista):
#     for i in lista:
#         s = ''.join(i)
#         if s == s[::-1]:
#             print("palindrome")
#         else:
#             print("nope")
#
# palindrome(lista)