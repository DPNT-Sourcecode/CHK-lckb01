from math import floor


class CheckoutSolution:

    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15,
                       "E": 40, "F": 10, "G": 20, "H": 10,
                       "I": 35, "J": 60, "K": 80, "L": 90,
                       "M": 15, "N": 40, "O": 10, "P": 50,
                       "Q": 30, "R": 50, "S": 30, "T": 20,
                       "U": 40, "V": 50, "W": 20, "X": 90,
                       "Y": 10, "Z": 50}
        self.offers = {"A":[{"quantity": 5, "price": 200}, {"quantity": 3, "price": 130}],
                       "B": [{"quantity": 2, "price": 45}],
                       "E": [{"quantity": 2, "price": 80, "free": "B"}],
                       "F": [{"quantity": 3, "price": 20}],
                       "H": [{"quantity": 10, "price": 80}, {"quantity": 5, "price": 45}],
                       "K": [{"quantity": 2, "price": 150}],
                       "N": [{"quantity": 3, "price": 120, "free": "M"}],
                       "P": [{"quantity": 5, "price": 200}],
                       "Q": [{"quantity": 3, "price": 80}],
                       "R": [{"quantity": 3, "price": 150, "free": "Q"}],
                       "U": [{"quantity": 4, "price": 120}],
                       "V": [{"quantity": 3, "price": 130}, {"quantity": 2, "price": 90}]
                       }
        self.total = {}
        self.reprocess = {}
    # skus = unicode string
    def checkout(self, skus:str):
        total = 0
        skus = "".join(sorted(skus))
        for sku in self.prices.keys():
            sku_count = skus.count(sku)
            self.total[sku] = dict(quantity=sku_count, price= self._calculate_cost(sku, sku_count) if sku_count > 0 else 0)
            skus = skus.replace(sku, "")
        for item in self.reprocess.keys():
            self._reprocess_item(item)
        total = self._calculate_total()
        self.reprocess = {}
        self.total = {}
        return -1 if skus else total

    def _calculate_total(self):
        total = 0
        for item in self.total.keys():
            total += self.total[item]["price"]
        return total


    def _calculate_cost(self, item: str, item_count:int):
        if item in self.offers.keys():
            offer_price = 0
            remainder_price = 0
            for offer in self.offers[item]:
                offer_count = floor(item_count / offer["quantity"])
                offer_price += offer_count * offer["price"]
                item_count -= offer["quantity"] * offer_count
                if offer.get("free", {}):
                    self.reprocess[offer["free"]] = offer_count
            remainder_price += item_count * self.prices[item]
            return offer_price + remainder_price
        else:
            return item_count * self.prices[item]

    def _reprocess_item(self, sku:str):
        if self.total[sku]["quantity"]:
            price_with_free = self._calculate_cost(sku, self.total[sku]["quantity"] - self.reprocess[sku])
            total_before = self.total[sku]["price"]
            self.total[sku]["price"] = price_with_free if total_before > price_with_free else price_with_free