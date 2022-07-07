def count_stair_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    if k <= 0:
        return 0
    res = 0
    for x in range(1, k + 1):
        res = res + count_k(n - x, k)
    return res


def even_weighted(s):
    """
    >>> even_weighted([1, 2, 3, 4, 5, 6])
    [0, 6, 20]
    """
    return [s[x] * x for x in range(len(s)) if x % 2 == 0]


def max_product(s):
    """
    Return the maximum product that can be formed using non-consecutive elements of s.

    >>> max_product([10,3,1,9,2]) #10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    if len(s) == 1:
        if s[0] > 1:
            return s[0]
        return 1

    candidates = []
    for x in range(len(s)):
        if x == 0:
            remained_list = s[2:]
            candidate = s[x] * max_product(remained_list)
            candidates += [candidate]
        else:
            remained_list = s[:x - 1] + s[x + 2:]
            candidate = s[x] * max_product(remained_list)
            candidates += [candidate]

    return max(candidates)
