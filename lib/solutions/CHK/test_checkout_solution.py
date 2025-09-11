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
        response = solution.checkout("EE")
        assert response == 80

    def test_buy_two_get_one_free(self):
        solution = CheckoutSolution()
        response = solution.checkout("FFFFFFF")
        assert response == 50
        response = solution.checkout("UUUUUUUUU")
        assert response == 280

    def test_other_free_item(self):
        solution = CheckoutSolution()
        response = solution.checkout("NNNMEEBRRRQ")
        assert response == 350

    def test_group_offers(self):
        solution = CheckoutSolution()
        response = solution.checkout("SSTXY")
        assert response == 85


if __name__ == '__main__':
    unittest.main()

