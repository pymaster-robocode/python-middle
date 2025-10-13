import time

def measure_time(func):
    def wrapper(arr):
        start = time.time()
        result = func(arr)
        end = time.time()
        print(f"{func.__name__} sorted for {end - start:.6f} secs")
        return result
    return wrapper