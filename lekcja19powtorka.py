# import string
#
#
# def func1():
#     return list(range(1,100))
#
# def func2():
#     return list(string.ascii_letters)
#
# def func3():
#     return dict(zip(func1(), func2()))
#
# def func4():
#     x = func3()
#     z = []
#     for i in range(1,len(x)+1):
#         if i % 2 == 0:
#             z.append(x.get(i))
#     print(z)
# func4()
#
#
# def func5():
#     return print(dict(zip(list(range(0,100)), list(string.ascii_letters))))
# func5()
import random
import string


#
#
# def func1():
#     return list(string.ascii_letters)
#
# def func2():
#     return random.choice(func1())
#
# def func3(x):
#     return x.append(func2())
#
#
import time


def func1():
    return list(range(0,10000))

def func2():
    return random.choice(func1())

def func3():
    z = []
    for i in range(0,10000):
        x = func2()
        if x % 2 == 1:
            z.append(x)
        else:
            z.append(x+1)
    print(len(z))
    print(z)


def func4():
    b = [1,5,2,3,4,5,5,5,6,7,8,8,8,9,10]
    g = set()
    for i in range(0,len(b)-1):
        if b[i] != b[i+1]:
            g.add(b[i])
        else:
            pass
    print(g)
# func4()



def func_powt():
    b = [1,1,1,2,2,2,3,3,3,5,5,5,1,6,6,6,6,4,4,4,8,9]
    g = set()
    for i in b:
        g.add(i)
    print(g)

# func_powt()


'''
chciałbym byś napisał mi funkcje która tworzy listę liczb całkowytych randomowo ustawionych i aby było zabawnie to ma tworzyć
listę na 100 elementów i jako print example poniżej:

'''




def funcer1():
    b = []
    for i in range(0,101):
        b.append(random.randint(0,500))
    for i in range(0,len(b)-1):
        print(f"{i+1}st element from list is : {b[i]}")

# funcer1()





import pyautogui
import os






# def funcer2():
#     x = 0
#     y = 0
#     for i in range(0,200):
#         x = x+5
#         y = y+5
#         pyautogui.moveTo(x, y)


def funcer2():

    # #biblioteka os :)
    # os.startfile(r"path\to\file\nawet\exe")
    #
    # #do poruszania się myszką
    # pyautogui.moveTo(750,80)
    #
    #
    # #do kliknięcia myszką
    # pyautogui.click()
    # pyautogui.doubleClick()
    # pyautogui.moveTo(750,150)
    # pyautogui.click()
    #
    # #do pisania tekstu
    # pyautogui.write("Hello World")
    #
    # #do złożonych operacji
    # with pyautogui.hold("ctrl"):
    #     pyautogui.press("s")
    pass


time.sleep(3)
while True:
    pyautogui.moveTo(950,600)
    pyautogui.rightClick()
    pyautogui.moveTo(200,150)
    pyautogui.rightClick()



# os.mkdir(r"C:\Users\AG\Desktop\PRACA\LEKCJE\LEK1.0\helloer")
# os.system("date")




# funcer2()