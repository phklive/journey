from doctest import run_docstring_examples

def fib(n):
    """Return the n'th Fibonacci number.
    
    >>> fib(2)
    1
    >>> fib(50)
    7778742049
    """
    pred, curr = 0, 1
    counter = 2
    while counter != n:
        pred, curr = curr, pred + curr
        counter += 1

    return curr

def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'

run_docstring_examples(fib, globals(), True)