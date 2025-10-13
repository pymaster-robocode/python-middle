import heapq
import random
import time

tasks = [
    (2, "Send report"),
    (1, "Fix critical bug"),
    (4, "Email client"),
    (2, "Code review")
]

heapq.heapify(tasks)

heapq.heappush(tasks, (3, "Deploy to prod"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Pr: {priority} || Task: {task}")

logs1 = ["2025-08-28 A", "2025-08-30 C"]
logs2 = ["2025-08-29 B", "2025-08-31 D"]
for line in heapq.merge(logs1, logs2):
    print(line)


def top_k_products(filename, k):
    heap = []
    with open(filename, 'r') as f:
        for line in f:
            name, count = line.strip().split()
            count = int(count)

            if len(heap) < k:
                heapq.heappush(heap, (count, name))
            else:
                heapq.heappushpop(heap, (count, name))

    return sorted(heap, key=lambda x: x[0], reverse=True)


top_products = top_k_products('sales.txt', 3)
for count, name in top_products:
    print(f"{name}: {count}")

n = 10_000_000
k = 10
data = [random.randint(1, 1_000_000) for _ in range(n)]

start = time.time()
top_sorted = sorted(data)[-k:]
end = time.time()
print("Sort:", end - start)

start = time.time()
top_heap = heapq.nlargest(k, data)
end = time.time()
print("heapq:", end - start)
