def pretty_print(lst: list, depth=1) -> str:
    parts = []
    for x in lst:
        parts.append(pretty_print(x, depth + 1) if type(x) is list else repr(x))
    return '[' + (',\n' + ' ' * depth).join(parts) + ']'

if __name__ == '__main__':
    data = [1, 2, ['hello', 'world', [3, 4 ,5]], 6]
    print(pretty_print(data))
