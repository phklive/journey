def cascade(n):
    print(n)
    if n >= 10:
        print(n)
        cascade(n // 10)
        print(n)

cascade(348392)
