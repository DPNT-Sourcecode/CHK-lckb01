from math import floor


class CheckoutSolution:

    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
        self.offers = {"A":[{"quantity": 5, "price": 200}, {"quantity": 3, "price": 130}],
                       "B": [{"quantity": 2, "price": 45}],
                       "E": [{"quantity": 2, "price": 80, "free": "E"}]
                       }
        self.total = {}
    # skus = unicode string
    def checkout(self, skus:str):
        total = 0
        for sku in self.prices.keys():
            sku_count = skus.count(sku)
            self.total[sku] = dict(quantity=sku_count, price= self._calculate_cost(sku, sku_count))
            total += self._calculate_cost(sku, skus.count(sku))
            skus = skus.replace(sku, "")
        return -1 if skus else total


    def _calculate_cost(self, item: str, item_count:int):
        if item in self.offers:
            offer_price = 0
            remainder_price = 0
            for offer in self.offers[item]:
                offer_count = floor(item_count / offer["quantity"])
                offer_price += offer_count * offer["price"]
                item_count -= offer["quantity"]
            remainder_price += item_count * self.prices[item]
            return offer_price + remainder_price
        else:
            return item_count * self.prices[item]

