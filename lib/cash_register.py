#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, name, price, quantity=1):
        price = float(price)
        quantity = int(quantity)
        self.total += price * quantity
        for i in range(int(quantity)):
            self.items.append(name)
        self.last_transaction = {"price": price, "quantity": quantity}

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        return self.total

    def void_last_transaction(self):
        self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
        for _ in range(self.last_transaction["quantity"]):
            self.items.pop()
