def print_delayed(x):
    """Return a new function. This new function, when called,
will print out x and return another function with the same
behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned
    """

    def delay_print(y):
        print(x)
        return print_delayed(y)

    return delay_print


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """

    def inner_print(x):
        if ________________________
            print("done")

        else:
            print(x)
        return ____________________

    return inner_print
