"""
Implement the following functions, at least enough to get the tests to pass.

Try implementing each from scratch, but also once you've implement reduce, try implementing
them in terms of reduce!

As stretch goals:

    - Add more tests, and have them pass
    - Increase the flexibility of each function, e.g. enable my_map to operate over any iterable type
    - Implement more functions in terms of what you already have, e.g. "flatten", "unique", "group_by" etc. See https://lodash.com/docs/ for a long list of interesting utility functions.
"""

def reduce(f, xs, init=None):
    """
    Apply the function f cummulatively to the items of xs, reducing to a single value.

    If initializer is provided, use it as the first value. Otherwise, use only the
    values in xs.

    >>> reduce(lambda acc, x: acc + x, [1, 2, 3, 4])
    10
    >>> def mirror(d, x):
    ...     d[x] = x
    ...     return d
    >>> reduce(mirror, ['foo', 'bar'], {})
    {'foo': 'foo', 'bar': 'bar'}

    alternative:
    
    acc = None
    if init is None:
        acc = xs[0] # Todo make sure to handle an empty xs
        for x in xs[1:]:
            acc = f(acc, x)
    else:
        acc = init
        for x in xs:
            acc = f(acc, x)
    return acc 
    """
    xs = iter(xs) # transform xs into an iterator
    acc = next(xs) if init is None else init # if "init" is set the accumulator will be "init" else the accumulator will be xs[1], This must be done because if the accumulator is set then we want to iterate over all values, else we want to iterate starting from xs[1] and use the first value as an accumulator
    for x in xs:
        acc = f(acc, x)
    return acc

def product(nums):
    """
    Return the product of the given numbers

    >>> product([2, 3])
    6
    >>> product([-1.0, -1.0, -1.0])
    -1.0
    >>> product([])
    1

    alternative:

    acc = 1
    for num in nums:
        x *= num
    return x
    """
    return reduce(lambda acc, x: acc * x, nums, 1)


def my_map(f, xs):
    """
    Return a new list, with the function f applied to each item in the given list

    >>> my_map(lambda x: x * x, [1, 2, 3, 4])
    [1, 4, 9, 16]

    alternative:

    return [f(x) for x in xs]
    """
    def g(ys, x):
        ys.append(f(x))
        return ys
    return reduce(g, xs, [])


def my_filter(f, xs):
    """
    Given a predicate function f (a function which returns True or False) and a list
    xs, return a new list with only the items of xs where f(x) is True

    >>> my_filter(lambda x: x > 0, [-1, 3, -2, 5])
    [3, 5]
    >>> my_filter(lambda x: False, [1, 2])
    []

    alternative:

    return [x for x in xs if f(x)]
    """
    def g(ys, x):
        if f(x):
            ys.append(x)
        return ys
    return reduce(g, xs, [])

def my_zip(*iters):
    """
    Given one or more iterables of the same length, return a list of lists of them
    "zipped" together, ie grouped by index

    >>> my_zip('abc', 'def', (1, 2, 3))
    [['a', 'd', 1], ['b', 'e', 2], ['c', 'f', 3]]
    >>> my_zip(["hello", "world", "yo"], 'def', (1, 2, 3))
    [['hello', 'd', 1], ['world', 'e', 2], ['yo', 'f', 3]]
    >>> my_zip(["hello"], ["world"])
    [['hello', 'world']]

    alternative:

    l = []
    for i in range(len(iters)):
        l.append([x[i] for x in iters])
    return l
    """
    def g(acc, iter):
        for i, item in enumerate(iter):
            acc[i].append(item)
        return acc
    return reduce(g, iters, [[] for _ in range(len(iters[0]))])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print('ok')
