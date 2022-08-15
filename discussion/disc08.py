from operator import mul


def count_function_call(func):
    def counted(*args):
        counted.call_count += 1
        return func(*args)

    counted.call_count = 0
    return counted


def count_frames(func):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = func(*args)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


def memo(func):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return memoized


@count_function_call
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


##########
#  Link  #
##########

class Link:
    """A linked list with a first element and the rest."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __repr__(self):
        return link_expression(self)

    def __add__(self, other):
        return extend_link(self, other)

    def __len__(self):
        return 1 + len(self.rest)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
        self = self.rest
        return string + str(self.first) + '>'


def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


# def filter_link(f, s):
#     if s is Link.empty:
#         return s
#     else:
#         filtered = filter_link(f, s.rest)
#         if f(s.first):
#             return Link(s.first, filtered)
#         else:
#             return filtered


def join_link(s, separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return Link(Link.empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n - m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m - 1)
        if not with_m:
            return without_m
        return with_m + without_m


def print_partitions(n, m):
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))


##########
#  Tree  #
##########

class Tree:
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.label + right.label, (left, right))


def sum_labels(t):
    """Sum the labels of a Tree instance, which may be None."""
    return t.label + sum([sum_labels(b) for b in t.branches])


##########
#  Sets  #
##########

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2


class B:
    def __init__(self):
        print("boo!")
        self.a = []

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret


def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """

    if lnk is Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    res = Link(1, Link.empty)
    for i in range(len(lst_of_lnks)):
        if lst_of_lnks[i] is Link.empty:
            return Link.empty
        res.first *= lst_of_lnks[i].first
        lst_of_lnks[i] = lst_of_lnks[i].rest
    res.rest = multiply_lnks(lst_of_lnks)
    return res


def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk_ = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk_)
    >>> lnk_
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return

    cache, lnk.first = lnk.first, lnk.rest.first
    lnk.rest.first = cache

    flip_two(lnk.rest.rest)


def filter_link(link, f):
    """
    >>> link_ = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link_, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    StopIteration
    >>> list(filter_link(link_, lambda x: x % 2 != 0))
    [1, 3]
    """
    curr = link
    while curr is not Link.empty:
        if f(curr.first):
            yield curr.first
        curr = curr.rest


def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if not t:
        return

    if t.label % 2 != 0:
        t.label += 1

    for branch in t.branches:
        make_even(branch)


def square_tree(t):
    """
    Mutates a Tree t by squaring all its elements.

    >>> t = Tree(3, [Tree(4)])
    >>> square_tree(t)
    >>> t.label
    9
    >>> t.branches[0].label
    16
    """
    if not t:
        return

    t.label *= t.label
    for branch in t.branches:
        square_tree(branch)


def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    res = []

    if t.label == entry:
        res.append([t.label])

    for branch in t.branches:
        paths = find_paths(branch, entry)

        for path in paths:
            new_path = [t.label] + path
            res.append(new_path)

    return res


def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1 and t2:
        tree = Tree(combiner(t1.label, t2.label))

        for x, y in zip(t1.branches, t2.branches):
            subtree = combine_tree(x, y, combiner)

            if tree.branches:
                tree.branches += subtree
            else:
                tree.branches = [subtree]

        return tree


def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    if t and t.label:
        t.label = map_fn(t.label)

        for branch in t.branches:
            for deeper in branch.branches:
                alt_tree_map(deeper, map_fn)

    return t
