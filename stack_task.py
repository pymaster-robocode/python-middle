import random
from stack import Stack
import time


class MoneyPile:
    def __init__(self):
        self.capacity = 5
        self.pile_stack = Stack()

    def put_money(self, nominal):
        if self.capacity > 0:
            self.pile_stack.push(nominal)
            self.capacity -= 1
        else:
            print("Stack is full!")

    def get_money(self):
        if not self.pile_stack.is_empty():
            self.capacity += 1
            nominal_got = self.pile_stack.pop()
            print("Got money of nominal: ", nominal_got)
        else:
            print("No money(")


pile = MoneyPile()
while True:
    if random.randint(0, 1):
        print("Put some money!")
        pile.put_money(random.choice([5, 10, 20, 50, 100, 200]))
    else:
        print("Trying to get some money!")
        pile.get_money()
    pile.pile_stack.display()
    time.sleep(1)
