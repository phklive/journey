

def vec_init(x, y):
    return [x, y]


def vec_str(v1):
    return f'<{v1[0]}, {v1[1]}>'


def vec_magnitude(v1):
    """Return the magnitude of the vector"""
    return (v1[0]**2 + v1[1]**2)**0.5


def vec_mul(v1, s):
    """Scalar multiplication"""
    return vec_init(s * v1[0], s * v1[1])


def vec_equals(v1, v2):
    return v1[0] == v2[0] and v1[1] == v2[1]


def vec_add(v1, v2):
    return vec_init(v1[0] + v2[0], v1[1] + v2[1])


def vec_sub(v1, v2):
    return vec_init(v1[0] - v2[0], v1[1] - v2[1])


def vec_neg(v1):
    return vec_init(-v1[0], -v1[1])


if __name__ == '__main__':
    v1 = vec_init(3, 2)
    v2 = vec_init(1, 1)
    v3 = vec_init(3, 4)

    assert vec_magnitude(v2) == 2**0.5
    assert vec_magnitude(v3) == 5
    assert vec_equals(vec_mul(v1, 2), vec_init(6, 4))
    assert vec_equals(vec_add(v1, v2), vec_init(4, 3))
    assert vec_equals(vec_sub(v1, v2), vec_init(2, 1))
    assert vec_equals(vec_neg(v1), vec_init(-3, -2))

    print(vec_str(v3))
    print('ok')
