'''

def func1():
    b = open("texter.txt", "a")
    d = []
    for i in range(0,5):
        d.append(input())
    b.write(f"{d}")


def func2():
    while True:
        func1()

# func2()


def func3():
    print(1800*12)

# func3()
'''
'''
plik VBS


DO
    python <plikpythonowy.py>
LOOP

        Visual Basic
            makro
DO
        
LOOP 
'''
'''

def func1():
    b = open("text.txt","a")
    index = str(input("Wpisz swoje imie "))
    b.write(f" Hello {index}")
    b.close()
    c = open("text.txt","r")
    for i in c:
        print(i)


# func1()
'''
'''
    mamy 3 skróty w formacie plików 
    
    r - read (pozwala na odczyt, ale nie zapis)
    w - write (pozwala na zapis, ale nie odczyt, natomiast ZAPIS JEST STAŁY)
    a - append (pozwala na ciągły nadpis pliku z zachowaniem poprzedniej zawartości)
    
'''

