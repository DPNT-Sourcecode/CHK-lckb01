import unittest

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = CheckoutSolution()
        response = solution.checkout("AAABCD")
        assert response == 195# add assertion here


if __name__ == '__main__':
    unittest.main()
