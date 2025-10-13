from dataclasses import dataclass
from typing import Optional, Iterator, Iterable


@dataclass
class Node:
    value: any
    next: any = None

class LinkedList:
    def __init__(self, iterable = None):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0
        if iterable is Iterable:
            for x in iterable:
                self.append(x)
        else:
            self.append(iterable)

    def __iter__(self) -> Iterator:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __repr__(self) -> str:
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> any:
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("LinkedList index out of range")
        cur = self.head
        for _ in range(index):
            assert cur is not None
            cur = cur.next
        assert cur is not None
        return cur.value

    def __contains__(self, value: any) -> bool:
        return self.find_node(value) is not None

    def append(self, value: any) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, value: any) -> None:
        node = Node(value, next=self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1

    def insert_at(self, index: int, value: any) -> None:
        if index <= 0:
            self.prepend(value)
            return
        if index >= self._size:
            self.append(value)
            return
        prev = self.head
        for _ in range(index - 1):
            assert prev is not None
            prev = prev.next
        node = Node(value, next=prev.next)
        prev.next = node
        self._size += 1

    def remove(self, value: any) -> bool:
        prev = None
        cur = self.head
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next is None:
                    self.tail = prev
                self._size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def find_node(self, value: any) -> Optional[Node]:
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None


# створюємо список з масиву
ll = LinkedList([1, 2, 3])
print(ll)  # LinkedList([1, 2, 3])

# append – додаємо в кінець
ll.append(4)
print(ll)  # LinkedList([1, 2, 3, 4])

# prepend – додаємо на початок
ll.prepend(0)
print(ll)  # LinkedList([0, 1, 2, 3, 4])

# insert_at – вставка за індексом
ll.insert_at(2, 99)
print(ll)  # LinkedList([0, 1, 99, 2, 3, 4])

# remove – видалення за значенням
ll.remove(99)
print(ll)  # LinkedList([0, 1, 2, 3, 4])

# find_node – знайти вузол
node = ll.find_node(3)
print(node)  # Node(value=3, next=Node(...))

# __contains__ – оператор in
print(3 in ll)   # True
print(10 in ll)  # False

# __getitem__ – доступ по індексу
print(ll[0])   # 0
print(ll[2])   # 2
print(ll[-1])  # 4 (підтримує від’ємні індекси)

# __len__ – довжина
print(len(ll))  # 5

# __iter__ – перетворення в list
print(list(ll))  # [0, 1, 2, 3, 4]

# працює і в циклі
for value in ll:
    print(value, end=" ")  # 0 1 2 3 4


# створюємо історію браузера
history = LinkedList()

# користувач переходить на сайти
for site in ["google.com", "youtube.com", "wikipedia.org", "github.com", "robocode.ua", "chat.openai.com"]:
    history.append(site)
    if len(history) > 5:   # обмежуємо максимум 5
        history.remove(history[0])

print("Історія браузера:", list(history))
# ['youtube.com', 'wikipedia.org', 'github.com', 'robocode.ua', 'chat.openai.com']

# дивимось останній сайт
print("Останній сайт:", history[-1])  # chat.openai.com

# перевіряємо чи був користувач на сайті
print("Був на github.com?", "github.com" in history)  # True
print("Був на facebook.com?", "facebook.com" in history)  # False

# видаляємо сайт вручну
history.remove("github.com")
print("Після видалення:", list(history))
# ['youtube.com', 'wikipedia.org', 'robocode.ua', 'chat.openai.com']
