def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

print(factorial(4))
print(factorial_iter(4))
