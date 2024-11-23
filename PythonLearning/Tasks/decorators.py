from functools import wraps

cache = {}
def cache_result(func):
    @wraps(func)
    def inner(*args, **kwargs):
        values = []
        global cache
        for i in args:
            values.append(str(i))
        for k, v in kwargs.items():
            values.append(str(k) + ':' + str(v))
        values = ";".join(values)
        for k, v in cache.items():
            if values in v:
                print(f"[FROM CACHE] Вызов {inner.__name__} = {k}")
                return k
        res = func(*args, **kwargs)
        cache[res] = values
        return res
    return inner