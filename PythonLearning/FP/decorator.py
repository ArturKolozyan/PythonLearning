from functools import wraps


def decorator_test(x=None):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f"{x}")
            return func(*args, **kwargs)
        return inner
    return decorator


@decorator_test(5)
def summ(a, b):
    return a + b


print(summ(5, 5))
