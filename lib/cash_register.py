#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        '''Initialize a cash register with an optional discount percentage.'''
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        '''Add items to the register with a specified title, price, and optional quantity.'''
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def void_last_transaction(self):
        '''Remove the last added item from the total and items list.'''
        if self.items:
            self.total -= self.last_transaction
            self.last_transaction = 0

    def apply_discount(self):
        '''Apply a discount to the total based on the set discount percentage.'''
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print("After the discount, the total comes to ${:d}.".format(int(self.total)))
            #print(f"After the discount, the total comes to ${int(self.total)}.")

        else:
            print("There is no discount to apply.")



# Example usage and testing
# Example usage
'''if __name__ == "__main__":
    register = CashRegister(20)
    register.add_item("macbook air", 1000)
    print(register.apply_discount())  # Should return: After the discount, the total comes to $800.
    register.add_item("eggs", 1.99, 2)
    print(register.total)  # Should print 803.98
    register.void_last_transaction()
    print(register.total)  # Should print 800'''





