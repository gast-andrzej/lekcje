import random
import string



class hello:

    def func1(self=None):
        return list(string.ascii_letters)

    def func12(self=None):
        return list(string.digits)

    def func2(self=None):
        n = 25
        z = hello.func1()
        x = hello.func12()
        char = list(string.punctuation)
        y = z + x + char
        haslo = []
        for i in range(0, n):
            haslo.append(random.choice(y))
        passwd = ''.join(str(i) for i in haslo)
        return passwd

    def __init__(self):
        hello.func2()



class generator_hasel:

    def func1(self, n):
        b = open("passwd.txt", "a")
        for i in range(0,n):
            b.write(f"{hello.func2()}\n")

    def __init__(self, n):
        self.n = n
        generator_hasel.func1(self, n)




