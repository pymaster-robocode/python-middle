class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        print("--------")
        while current:
            print(current.value, end="\n")
            current = current.next
        print("--------\n")

"""
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("POP:", stack.pop())
stack.display()
"""