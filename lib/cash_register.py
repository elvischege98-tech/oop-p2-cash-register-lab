#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

        # validate discount
        self.discount = discount

    # ---------- DISCOUNT PROPERTY ----------
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    # ---------- ADD ITEM ----------
    def add_item(self, title, price, quantity=1):
        item_total = price * quantity

        self.total += item_total

        # store item (including multiples)
        self.items.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

        # track transaction
        self.previous_transactions.append(item_total)

    # ---------- APPLY DISCOUNT ----------
    def apply_discount(self):
        if self.total == 0:
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        print(f"Success! New total: {self.total:.2f}")

    # ---------- VOID LAST TRANSACTION ----------
    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_amount = self.previous_transactions.pop()
        self.total -= last_amount

        # remove last item occurrence
        if self.items:
            self.items.pop()

        # ensure total doesn't go negative
        if not self.items:
            self.total = 0.0

    # ---------- GET ITEMS ----------
    def get_items(self):
        return self.items