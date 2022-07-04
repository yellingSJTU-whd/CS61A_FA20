def multiply(m, n):
    """ Implements multiply in a recursion way.
    >>> multiply(5,3)
    15
    """
    if n == 1:
        return m
    return m + multiply(m, n - 1)


def hailstone(n):
    """ Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    assert n > 0
    print(n)

    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n // 2)
    return 1 + hailstone(3 * n + 1)


def merge(n1, n2):
    """ Merges two numbers.
    >>> merge(31,42)
    4321
    >>> merge(21,0)
    21
    >>> merge(21,31)
    3211
    """

    def process_digits(num):
        smallest_digit, index, i = 10, 0, 0
        stringify = str(num)
        while i < len(stringify):
            curr_digit = int(stringify[i])
            if curr_digit < smallest_digit:
                smallest_digit = curr_digit
                index = i
            i += 1
        return smallest_digit, index

    def extract_digit(num, i):
        stringify = str(num)
        if len(stringify) == 1:
            return 0
        low = stringify[i + 1:]
        if i == 0:
            return int(low)
        high = stringify[:i]
        return int(high + low)

    if n1 == 0 and n2 == 0:
        return None
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    smallest_digit1, index1 = process_digits(n1)
    smallest_digit2, index2 = process_digits(n2)

    if smallest_digit1 <= smallest_digit2:
        return merge(extract_digit(n1, index1), n2) * 10 + smallest_digit1
    return merge(n1, extract_digit(n2, index2)) * 10 + smallest_digit2


def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x:x+1,1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    def repeat(n):
        if n > 0:
            return f(repeat(n - 1))
        else:
            return x

    return repeat


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """

    def prime_helper(num, i):
        if num <= i:
            return num != 1
        elif num % i == 0:
            return False
        else:
            return prime_helper(num, i + 1)

    return prime_helper(n, 2)
