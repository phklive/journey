def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient balance'
        balance -= amount
        return balance
    return withdraw
