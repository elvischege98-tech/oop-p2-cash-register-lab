#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

        # validate discount using property
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

        # update total (keeps previous total)
        self.total += item_total

        # store item (including duplicates)
        for _ in range(quantity):
            self.items.append(title)

        # store transaction for undo
        self.previous_transactions.append(item_total)

    # ---------- APPLY DISCOUNT ----------
    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        print(f"Success! New total: {self.total}")

    # ---------- VOID LAST TRANSACTION ----------
    def void_last_transaction(self):
        if not self.previous_transactions:
            self.total = 0.0
            return

        last_amount = self.previous_transactions.pop()
        self.total -= last_amount

        # remove last items added
        if self.items:
            # remove last added items based on quantity assumption
            self.items.pop()

        # reset if empty
        if not self.items:
            self.total = 0.0

    # ---------- RETURN ITEMS ----------
    def get_items(self):
        return self.items