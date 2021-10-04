def is_prime(n):
    '''
    Determina daca un numar dat este prim.
    :param n: Numar natural.
    :return: True daca acesta este numar prim, False in caz contrar.
    '''
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True


def get_largest_prime_below(n):
    '''
    Ex. 1) Determina ultimul numar prim mai mic decat un numar dat.
    :param n: Numar natural.
    :return: Returneaza numarul.
    '''
    for i in reversed(range(n)):
        if is_prime(i):
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(5) == 3
    assert get_largest_prime_below(12) == 11
    assert get_largest_prime_below(17) == 13
    assert get_largest_prime_below(22) == 19
    assert get_largest_prime_below(35) == 31
    assert get_largest_prime_below(40) == 37
    assert get_largest_prime_below(45) == 43
    assert get_largest_prime_below(70) == 67
    assert get_largest_prime_below(1000) == 997


test_get_largest_prime_below()


def is_superprime(n) -> bool:
    '''
    Ex. 6) Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
    :param n: Numar natural.
    :return: returneaza True daca acesta este superprim, False in caz contrar.
    '''
    if is_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
    else:
        return False
    return True


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(13) is False
    assert is_superprime(17) is False
    assert is_superprime(18) is False
    assert is_superprime(93) is False
    assert is_superprime(21) is False
    assert is_superprime(33) is False
    assert is_superprime(53) is True
    assert is_superprime(59) is True
    assert is_superprime(71) is True


test_is_superprime()

shouldRun = True
while shouldRun:
    print("1. Determinati ultimul numar prim mai mic decat un numar dat.")
    print("2. Determinati dacă un număr este superprim: dacă toate prefixele sale sunt prime.")
    print("x. Iesire")

    optiune = input("Alegeti optiunea: ")
    if optiune == "1":
        n = int(input("Inserati un numar: "))
        print(get_largest_prime_below(n))
    elif optiune == "2":
        n = int(input("Inserati un numar: "))
        if is_superprime(n):
            print("Numarul ", n, " este superprim.")
        else:
            print("Numarul ", n, " nu este superprim.")
    elif optiune == "x":
        shouldRun = False
    else:
        print("Optiune gresita! Reincercati!")
