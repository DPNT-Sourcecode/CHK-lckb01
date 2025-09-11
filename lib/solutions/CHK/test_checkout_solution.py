import unittest

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class MyTestCase(unittest.TestCase):
    def test_abcd(self):
        solution = CheckoutSolution()
        response = solution.checkout("ABCD")
        assert response == 115# add assertion here

    def test_multiple_a(self):
        solution = CheckoutSolution()
        response = solution.checkout("AAAAAAA")
        assert response == 300# add assertion here

    def test_multiple_b(self):
        solution = CheckoutSolution()
        response = solution.checkout("BBBBBBB")
        assert response == 165

    def test_multiple_c(self):
        solution = CheckoutSolution()
        response = solution.checkout("CCCCCCC")
        assert response == 140

    def test_multiple_d(self):
        solution = CheckoutSolution()
        response = solution.checkout("DDDDDDD")
        assert response == 105

    def test_return_negative_one_on_unknown_sku(self):
        solution = CheckoutSolution()
        response = solution.checkout("AAAAAAAa")
        assert response == -1
        response = solution.checkout("AAAAAAAE")

    def test_return_correct_value_when_other_offer_affects_another_item(self):
        solution = CheckoutSolution()
        response = solution.checkout("BBBBBBBEE")
        assert response == 215

    def test_blah(self):
        solution = CheckoutSolution()
        response = solution.checkout("A")
        assert response == 50
        response = solution.checkout("AA")
        assert response == 100

if __name__ == '__main__':
    unittest.main()


