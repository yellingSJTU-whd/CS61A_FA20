def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """

    def f(g):
        nonlocal n
        n = g(n)
        return n

    return f


def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])


p = [2, 3]
q = [4, [p]]
mystery(q, p)


def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """

    grouped = {}
    for element in s:
        key = fn(element)
        if key in grouped:
            grouped[key] += [element]
        else:
            grouped[key] = [element]

    return grouped


def add_this_many(x, el, s):
    """
    Adds el to the end of s the number of times x occurs in s.

    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """

    i, origin_len = 0, len(s)
    while i < origin_len:
        if s[i] == x:
            insertion_index = len(s)
            s[insertion_index:insertion_index] = [el]
        i += 1


def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to fulter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1,100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for x in iterable:
        if fn(x):
            filtered = x
            yield filtered
