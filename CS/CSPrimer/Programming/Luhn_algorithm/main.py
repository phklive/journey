import unittest

LOOKUP = {
    "0": 0,
    "1": 2,
    "2": 4,
    "3": 6,
    "4": 8,
    "5": 1,
    "6": 3,
    "7": 5,
    "8": 7,
    "9": 9,
}

def add_check_digit(payload: str) -> str:
    """
    Adds a check digit add the end of the inputed payload.
    """
    total = 0
    for i, d in enumerate(reversed(payload)):
        total += LOOKUP[d] if i % 2 == 0 else int(d)
    return payload + str(10 - (total % 10))


def verify(number: str) -> bool:
    """
    Checks if the number has a valid checksum.
    """
    payload = number[:-1]
    return add_check_digit(payload)[-1] == number[-1]

class TestLuhn(unittest.TestCase):
    def test_add_check_digit_function(self):
        self.assertEqual(add_check_digit("1789372997"), "17893729974")

    def test_verify_function(self):
        self.assertTrue(verify("17893729974"))
        self.assertFalse(verify("17893729973"))
        self.assertFalse(verify("17893729975"))

if __name__ == '__main__':
    unittest.main()
