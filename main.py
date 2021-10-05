from typing import Union


def findprimes(n):
    '''
    Determina numerele prime pana la n.
    :param n: Parametru de intrare, numar natural, reprezinta limita superioara a listei.
    :return: Returneaza lista cu numerele prime pana la n.
    '''
    primes = list(range(2, n + 1))
    for i in primes:
        j = 2
        while i * j <= primes[-1]:
            if i * j in primes:
                primes.remove(i * j)
            j = j + 1
    return primes


def get_goldbach(n) -> Union[(int, int)]:
    '''
    Ex. 3) Determină numerele prime p1 si p2 astfel încât n = p1 + p2 (verificarea conjecturii lui Goldbach), p1 minim și p2 maxim.
    :param n: Parametru de intrare, numar natural, folosit pentru a determina cele 2 numere prime.
    :return: Returneaza p1 si p2(numerele prime, astfel incat n = p1 + p2).
    '''
    if n % 2 == 0 and n > 3:
        prime = findprimes(n)
        for i in range(len(prime)):
            p1 = prime[i]
            for j in range(len(prime)):
                p2 = prime[j]
                result = p1 + p2
                if result == n:
                    return p1, p2
    else:
        return print("Nu exista solutie.")


def test_get_goldbach():
    assert get_goldbach(4) == (2, 2)
    assert get_goldbach(6) == (3, 3)
    assert get_goldbach(8) == (3, 5)
    assert get_goldbach(10) == (3, 7)
    assert get_goldbach(12) == (5, 7)
    assert get_goldbach(14) == (3, 11)
    assert get_goldbach(16) == (3, 13)
    assert get_goldbach(18) == (5, 13)
    assert get_goldbach(20) == (3, 17)
    assert get_goldbach(22) == (3, 19)
    assert get_goldbach(24) == (5, 19)
    assert get_goldbach(26) == (3, 23)
    assert get_goldbach(28) == (5, 23)
    assert get_goldbach(30) == (7, 23)
    assert get_goldbach(32) == (3, 29)


test_get_goldbach()


def get_newton_sqrt(n, steps) -> float:
    '''
    Ex. 4) Execută un număr dat de pași pentru a calcula radicalul unui număr dat folosind metoda lui Newton cu x0=2 și afișează aproximarea obținută.
    :param n: Parametru de intrare, numar natural, care reprezinta numarul caruia algoritmul ii calculeaza radicalul.
    :param steps: Parametru de intrare, numar natural, care reprezinta numarul pasilor in vederea calcului radicalului.
    :return: Returneaza n, care retine valoarea radicalului.
    '''
    a = float(n)
    for i in range(steps):
        n = 0.5 * (n + a / n)
    return n


def test_get_newton_sqrt():
    assert get_newton_sqrt(9, 10) == 3.0
    assert get_newton_sqrt(9, 9) == 3.0
    assert get_newton_sqrt(9, 8) == 3.0
    assert get_newton_sqrt(9, 7) == 3.0
    assert get_newton_sqrt(9, 6) == 3.0
    assert get_newton_sqrt(10, 13) == 3.162277660168379
    assert get_newton_sqrt(10, 1) == 5.5
    assert get_newton_sqrt(15, 10) == 3.872983346207417
    assert get_newton_sqrt(25, 5) == 5.000023178253949
    assert get_newton_sqrt(25, 10) == 5.0
    assert get_newton_sqrt(37, 8) == 6.08276253029822
    assert get_newton_sqrt(42, 10) == 6.48074069840786


test_get_newton_sqrt()

shouldRun = True
while shouldRun:
    print('1. Determinati numerele prime p1 si p2 astfel incat n = p1 + p2.')
    print("2. Determinati radicalul unui numar, folosind metoda lui Newton.")
    print("x. Iesire.")
    optiune = input("Alegeti optiunea: ")
    if optiune == "1":
        n = int(input("Inserati un numar: "))
        print(get_goldbach(n))
    elif optiune == "2":
        n = int(input("Inserati un numar:"))
        steps = int(input("Inserati un numar de pasi:"))
        print("Radicalul numarului ", n, " este ", get_newton_sqrt(n, steps))
    elif optiune == "x":
        shouldRun = False
    else:
        print("Optiune gresita! Reincercati!")
