
class Vec(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def magnitude(self):
        """Return the magnitude of the vector"""
        return (self.x**2 + self.y**2)**0.5

    def __mul__(self, s):
        """Scalar multiplication"""
        return Vec(s * self.x, s * self.y)

    def __eq__(self, v2):
        return self.x == v2.x and self.y == v2.y

    def __add__(self, v2):
        return Vec(self.x + v2.x, self.y + v2.y)

    def __sub__(self, v2):
        return Vec(self.x - v2.x, self.y - v2.y)

    def __neg__(self):
        return Vec(-self.x, -self.y)


class Displacement(Vec):
    def move(self, velocity, time):
        """
        Change the displacement by applying the given velocity for the given time

        e.g. vector (3, 2), if moved for 5 seconds at 1 m/s, would be (8, 7)
        """
        self.x = self.x + velocity * time
        self.y = self.y + velocity * time


if __name__ == '__main__':
    v1 = Vec(3, 2)
    v2 = Vec(1, 1)
    v3 = Vec(3, 4)

    assert v2.magnitude() == 2**0.5
    assert v3.magnitude() == 5
    assert v1 * 2 == Vec(6, 4)
    assert v1 + v2 == Vec(4, 3)
    assert v1 - v2 == Vec(2, 1)
    assert -v1 == Vec(-3, -2)

    d = Displacement(3, 2)
    d.move(1, 5)
    assert d == Vec(8, 7)

    print('ok')
