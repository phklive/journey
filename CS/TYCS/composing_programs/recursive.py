def sum_digits(n):
    """Return the sum of the digits of a positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

print(sum_digits(100))
print(sum_digits(451))
print(sum_digits(3))

"""
1. sum_digits(452)
2. sum_digits(45) + 2
3. sum_digits(4) + 5 + 2
4. 4 + 5 + 2
5. 11
"""
