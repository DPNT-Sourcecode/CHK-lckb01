from math import floor


class CheckoutSolution:

    def __init__(self):
        self.prices = {"A": 50, "B": 45, "C": 35, "D": 20}
        self.offers = {"A":{"quantity": 3, "price": 130}, "B": {"quantity": 2, "price": 45}}
    # skus = unicode string
    def checkout(self, skus:str):
        while skus:
            skus.count("A")
            skus.count("B")

    def _calculate_cost(self, item_count:int, item: str):
        if item in self.offers:
            return floor(item_count, self.offers[item]["quantity"])

