from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 3
od['c'] = 2

print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od.move_to_end('b')       # 'b' стане останнім
print(od)  # OrderedDict([('a', 1), ('c', 3), ('b', 2)])

od.move_to_end('c', last=False)  # 'c' стане першим
print(od)  # OrderedDict([('c', 3), ('a', 1), ('b', 2)])

item = od.popitem(last=False)
print(item)  # ('c', 3)
print(od)    # OrderedDict([('a', 1), ('b', 2)])

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Приклад
cache = LRUCache(3)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
print(cache.cache)  # OrderedDict([(1, 'A'), (2, 'B'), (3, 'C')])

cache.get(2)
cache.put(4, "D")
print(cache.cache)  # OrderedDict([(3, 'C'), (2, 'B'), (4, 'D')])



