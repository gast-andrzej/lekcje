'''
Rock Paper Scissor

zaprojektuj i napisz funkcje która dodaje do listy kolejne elementy z zewnątrz (wpisane przez użytkownika)
zaprojektuj i napisz funkcje która dodaje do listy kolejne elementy z zewnątrz (wpisane przez użytkownika ale tylko liczby)
zaprojektuj i napisz funkcje która wyrzuci nam ostatni integer z listy
zaprojektuj i napisz funkcje która wyrzuci nam ostatni element
zaprojektuj i napisz funkcje która wyrzuci nam ostatni string z listy
zaprojektuj i napisz funkcje która dodaje losowe elementy do listy
zaprojektuj i napisz funkcje która sumuje elementy liczbowe w liście i podaje ich najmniejszy wspólny nieparzysty dzielnik
wyższy od 18

zaprojektuj i napisz funkcje która sumuje elementy liczbowe w liście i podaje ich najmniejszy wspólny parzysty dzielnik
wyższy od 34
'''

# Rock Paper Scissor z licznikiem zwycięstw i możliwością przegrania
# korzystając z poznanych dotychczas rzeczy

import random
import string



def RPS():
    wyg = 0
    przeg = 0
    while True:
        if wyg < 5:
            if przeg < 5:
                los = random.randint(1, 3)
                inputer = int(input("1 Rock 2 Paper 3 Scissors"))
                if inputer == 1 and los == 1:
                    print("remis")
                elif inputer == 1 and los == 2:
                    print("ojć, :D")
                    przeg += 1
                elif inputer == 1 and los == 3:
                    print("Wygrana")
                    wyg += 1
                elif inputer == 2 and los == 1:
                    print("Wygrana")
                    wyg += 1
                elif inputer == 2 and los == 2:
                    print("remis")
                elif inputer == 2 and los == 3:
                    print("ojć, :D")
                    przeg += 1
                elif inputer == 3 and los == 1:
                    print("ojć :D")
                    przeg += 1
                elif inputer == 3 and los == 2:
                    print("Wygrana")
                    wyg += 1
                elif inputer == 3 and los == 3:
                    print("remis")
                else:
                    pass
            else:
                if przeg >= 5:
                    print("PRZEGRANA")
                    break
        else:
            if wyg >= 5:
                print("WYGRANA")
                break




def cezar():
    dexal = input("Wprowadź wiadomość do zakodowania bez polskich znaków \n"
                  ": ")
    turnex = int(input("value przesunięcia "))
    codex = []
    listaval = []
    listacrypta = []
    listacrypta2 = []
    for i in dexal:
        for j in i:
            codex.append(j)
    g = list(range(1,100))
    b = list(string.ascii_letters)
    b.append(" ")
    mac1 = dict(zip(g,b))
    mac2 = dict(zip(b,g))

    for i in codex:
        listaval.append(mac2.get(i))

    for i in listaval:
        gg = i + turnex
        if gg > 53:
            gg -= 53
        else:
            pass
        listacrypta.append(gg)
    for i in listacrypta:
        listacrypta2.append(mac1.get(i))

    textcode = ''.join(i for i in listacrypta2)

    print(mac1)
    print(mac2)
    print(codex)
    print(listaval)
    print(textcode)

cezar()

def menus():
    while True:
        print("Witaj w menu :) jaką grę chcesz odtworzyć?\n"
              "1 Rock Paper Scissors \n"
              "0 EXIT")
        indexer = input("Wybierz grę ")
        try:
            int(indexer)
            match int(indexer):
                case 0:
                    break
                case 1:
                    RPS()
        except:
            pass

# menus()