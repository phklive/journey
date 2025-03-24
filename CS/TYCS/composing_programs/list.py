list = [1,2,3,4,5]
doubled = [x * 2 for x in list]
even_squared = [x * x for x in list if x % 2 == 0]
odd_squared = [x * x for x in list if not x % 2 == 0]

print(list, doubled, even_squared, odd_squared)
