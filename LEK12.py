'''

Pytania początkowe:

-co to funkcja?

-co to rekurencja?

-do czego wykorzystuje się rekurencje?

-trochę o zmiennych globalnych hardcode!



Nowość:

-czym są zmienne strzeżone i do czego się je wykorzystuje

-czym są funkcje strzeżone i do czego się je wykorzystuje

-czym są funkcje statyczne i do czego się je wykorzystuje

-łączenie funkcji strzeżonych i rekurencji

-łączenie elementów w funkcje statyczne

ZADANKA :)

'''

# def staticfunc():
#
#     _sumakontrolna = 8080
#
#
#     def _func_sumakontrolna(k):
#         x = []
#         g = 0
#         y = 0
#         for i in range(0,5):
#             g = g+1
#             z = float(input(f"{g}"))
#             x.append(z)
#         for i in x:
#             y = y+i
#         if k == y:
#             print("Możesz wejść")
#             return True
#         else:
#             print("nieautoryzowany dostęp")
#             return False
#
#
#
#
#     def func_stat():
#         if _func_sumakontrolna(_sumakontrolna)==True:
#             print("hello")
#         else:
#             pass
#     func_stat()
#
# def func1():
#     c = list(range(0,101))
#     return c
#
# def func2():
#     _listaprzetworzona = []
#     _listy = func1()
#     for i in _listy:
#         if i%2==0:
#             j = i/2
#             _listaprzetworzona.append(j)
#         else:
#             _listaprzetworzona.append(i)
#     return _listaprzetworzona
#
#
# _suma_kontrolna = []
#
# def _randomizer():
#     c = func2()
#     seed = [4,5,6,4,5,1,2,3,4,9,7]
#     b = []
#     d = []
#     f = []
#     for i in seed:
#         if i%5==1:
#             b.append(i)
#         elif i%3==2:
#             d.append(i)
#         else:
#             f.append(i)
#     _suma_kontrolna.append(c[b[1]])
#     _suma_kontrolna.append(int(c[f[1]])*16)
#     _suma_kontrolna.append(c[int(d[0])*5])
#     _suma_kontrolna.append(c[int(d[0])*3])
#     _suma_kontrolna.append(c[int(d[0])*7])
#     _suma_kontrolna.append(c[int(d[1])*8])
#
#
#     return print(_suma_kontrolna)
#
# _randomizer()


'''
ZADANKA

Napisz mi funkcje strzeżoną która stworzy szereg losowych danych umieszczonych wewnątrz listy

napisz funkcje strzeżoną dwukrotności kwadratu elementów jako suma kontrolna z listy strzeżonej

zmodyfikuj func2 aby wypuszczała listę elementów od 0-9

napisz funkcje przyjmującą liczby tylko od 0-9 i zwracające je w formie listy na tyle elementów ile ma _lk

Napisz dowolną skomplikowaną funkcje tak skomplikowaną na ile się czujesz, która do swojego działania
będzie musiała wykorzystać funkcje rekurencyjną zabezpieczeń taką jak _func3 funkcja ta (_func3) musi być
importowana z innego pliku niż funkcja która ją wykorzystuje.


P.S.
Możesz użyć _func3 z zajęć ;)

'''

def _func1():
    _ls = list(range(0,101))
    return _ls

def _func2():
    _ls = _func1()
    _lk = []
    _sumao = 0
    for i in _ls:
        j = (i*i)*2
        _lk.append(j)
    for i in _lk:
        _sumao = _sumao+i

    _stri = f"{_sumao}"
    _stri.split()
    _lk = []
    for i in _stri:
        _lk.append(int(i))

    return _lk

def _func3():
    _aller = _func2()
    _sprt = []
    for i in range(0,len(_aller)):
        _inputer = int(input("Number "))
        _sprt.append(_inputer)
        # 6 7 6 7 0 0

    if _aller == _sprt:
        return True
    else:
        return False

def func4():
    b = _func3()
    if b is True:
        print("Hello")
    else:
        print("No")


func4()
