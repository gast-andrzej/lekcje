# import random
#
# b = ['Ada', 'Adamina', 'Adela', 'Adriana', 'Adrianna', 'Agata', 'Agnieszka', 'Alana', 'Aldona', 'Aleksandra', 'Alessandra', 'Alexandra', 'Alfreda', 'Alia', 'Alice', 'Alicja', 'Alina', 'Alisa', 'Aisha', 'Amalia', 'Amanda', 'Amelia', 'Anastasiia', 'Anastazja']
#
# print(f"{random.choice(b)}")
import os
import random
import string
import time

import openpyxl
import pandas
import pyautogui
import xlwt
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def func1():
    x = "CALKOWITY!"
    b = []
    for i in x:
        b.append(i)
    return print(len(b))

# func1()


x = "CALKOWITY!"

def func2(x):
    b = list()
    for i in x:
        b.append(i)
    return print(len(b))

# func2(x)

def func3():
    b = open("textowka.txt", "r")
    n = []
    g = []
    for j in b:
        for i in b.readline():
            n.append(i)
        g.append(len(n))
        n.clear()
    print(max(g))
    print(min(g))

# func3()


def func4():
    b = open("plikexcel.xlsx", "a")
    z = list(string.ascii_letters)
    for i in z:
        b.write(i)
    b.close()
    pandas.read_excel("plikexcel.xlsx")

# func4()











def func_master():
    c = random.randint(0,1000)
    x = 0
    while x <= 7:
        inputer = input("Wprowadź liczbę")
        try:
            int(inputer)
            if c > int(inputer):
                print("MAOOOOO")
                x += 1
            elif c < int(inputer):
                print("Ale śniegu NAEBAO")
                x += 1
            else:
                print("Ale urwał, aaa, ale to było dobre xD ")
                break
        except:
            print("daruj, wpisz liczbe")

# func_master()


def gener_passwd():
    literki = list(string.ascii_letters)
    znaki = "!@#$%^&*()_-+=/*-?><"
    lista_znakow = []
    passwd = []
    for i in znaki:
        for j in i:
            lista_znakow.append(j)
    for i in lista_znakow:
        passwd.append(i)
    g = ''.join(passwd)
    print(g)

# gener_passwd()



def func_generation():
    # lista_znakow = list(string.digits)
    # passwd = []
    # for i in range(0,4):
    #     passwd.append(str(random.randint(1000,9999)))
    # g = ''.join(passwd)


    # driver = webdriver.Chrome()
    # driver.get("http://www.google.com/")
    # # driver.quit()
    # time.sleep(5)
    pass


# func_generation()




def func_autoclicker():
    driver = webdriver.Chrome()
    driver.get("https://meet.google.com/pvf-hogp-rjv")
    time.sleep(7)
    pyautogui.moveTo()
    pyautogui.click()
    pyautogui.moveTo()
    pyautogui.write("ten FACET")
    pyautogui.moveTo()
    pyautogui.click()
    # time.sleep(10)
    pyautogui.moveTo()
    pyautogui.write("DUPA BISKUPA")
    pyautogui.press("enter")
    driver.quit()



while True:
    func_autoclicker()









