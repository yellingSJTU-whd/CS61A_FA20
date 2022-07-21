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
