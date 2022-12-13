'''
Napisz funkcje zwracającą listę w której są integery

Napisz funkcje zwracającą listę w której są stringi ascii letters

Napisz funkcje która tworzy dict dla ascii letters z wykorzystaniem 2 poprzednich funkcji
#
# Napisz funkcje która tworzy listę elementów od 0 do 100 korzystając z list comprehension

Napisz funkcje przyjmującą wartości z zewnątrz (wartości inputu (5) i wrzucające ją w TUPLE) funkcja ma zwracać tuple

Napisz funkcje wydzielającą elementy z tupli do elementów integerowych lub floatowych i sprawdzającą ich parzystość

Napisz funkcje która weźmie z poprzedniej funkcji elementy parzyste
    (w dowolnej formie) i zwróci listę zawierającą kwadraty tych elementów.



'''
import random
import string

def func1(n):
    z = list(range(0,n))
    return z

def func2():
    z = list(string.ascii_letters)
    return z

# func2()

def func3():
    z = dict(zip(func1(len(func2())), func2()))
    return print(z)


# func3()


'''
palindrome

napisz mi funkcje która sprawdzi czy element listy jest palindromem
'''
x = ['kajak', 121, 333, 456, 'kkl']

def palindrome(x):
    for i in x:
        z = str(i)

        if z == z[::-1]:
            print('palindrome')
        else:
            print('nope')

# palindrome(x)


def choinka():
    z = []
    for i in range(0,50):
        z.append(i)
    for i in z:
        if i == z[len(z)-1]:
            print(i*"@")
        elif i == 1:
            print("@")
        elif i % 2 == 0:
            print(i*"*")
        else:
            print(i*"$")

choinka()