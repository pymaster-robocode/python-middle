from collections import OrderedDict
from functools import wraps

def lru_cache_decorator(capacity=5):
    cache = OrderedDict()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                cache.move_to_end(key)
                result = cache[key]
                print(f"[CACHE HIT] Key: {key}, Cache: {list(cache.keys())}")
                return result

            result = func(*args, **kwargs)
            cache[key] = result

            if len(cache) > capacity:
                removed = cache.popitem(last=False)
                print(f"[CACHE EVICT] Removed: {removed}")

            print(f"[CACHE ADD] Key: {key}, Cache: {list(cache.keys())}")
            return result
        return wrapper
    return decorator


@lru_cache_decorator(capacity=3)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(4))
print(fib(3))
print(fib(5))
