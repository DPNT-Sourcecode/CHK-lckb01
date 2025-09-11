from math import floor


class CheckoutSolution:

    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        self.offers = {"A":{"quantity": 3, "price": 130}, "B": {"quantity": 2, "price": 45}}
    # skus = unicode string
    def checkout(self, skus:str):
        total = 0
        for sku in self.prices.keys():
            total += self._calculate_cost(sku, skus.count(sku))
            skus = skus.replace(sku, "")
        return -1 if skus else total



    def _calculate_cost(self, item: str, item_count:int):
        if item in self.offers:
            offer_price = floor(item_count /self.offers[item]["quantity"]) * self.offers[item]["price"]
            remainder_price = item_count % self.offers[item]["quantity"] * self.prices[item]
            return offer_price + remainder_price
        else:
            return item_count * self.prices[item]
