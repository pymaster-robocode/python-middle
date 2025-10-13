class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        while current:
            print(current.value, end=" -> \n")
            current = current.next


# Приклад
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()          # 10 -> 20 -> 30 -> None
print("dequeue:", queue.dequeue())
queue.display()          # 20 -> 30 -> None
