def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90,False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100,True)
    True
    """
    return temp < 60 or raining


def square(x):
    print("here!")
    return x * x


def so_slow(num):
    """
    >>> so_slow(5)
    ZeroDivisionError: division by zero
    """
    x = num
    while x > 0:
        x = x + 1
        return x / 0


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def square1(x):
    return x ** 2

