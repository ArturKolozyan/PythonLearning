from functools import wraps
from time import time


def work_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Время работы: {end_time - start_time:.10f}")
        return result
    return inner


@work_time
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2 + (low + high) % 2
        if lst[mid] == item:
            return mid
        if lst[mid] > item:
            high = mid - 1
        if lst[mid] < item:
            low = mid + 1
    else:
        return None


@work_time
def not_binary_search(lst, item):
    for i in lst:
        if i == item:
            return i
    return None


s = list(range(10*10**5))
print(binary_search(s, 100000))
print(not_binary_search(s, 100000))
