# Summation

def summation(n, term):
    total, k = 0, 1
    while  k <= n:
        total, k = total + term(k), k + 1
    return total

# Summation of naturals

def identity(x):
    return x

def sum_naturals(n):
    return summation(n, identity)

# Summation of cubes

def cube(x):
    return x * x * x

def sum_cubes(n):
    return summation(n, cube)

# Summation converging towards pi

def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

def pi_sum(n):
    return summation(n, pi_term)

print(sum_naturals(100))
print(sum_cubes(100))
print(pi_sum(100))
