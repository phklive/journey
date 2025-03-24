# Golden ratio

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def golden_update(guess):
    return 1 / guess + 1

phi = improve(golden_update, square_close_to_successor)

print(phi)

# Nested definitions

def average(x, y):
    return (x + y) / 2

def sqrt(a):
    def sqrt_update(x):
        return average(x, a / x)
    
    def sqrt_close(x):
        return approx_eq(x * x, a)

    return improve(sqrt_update, sqrt_close)

print(sqrt(256))
