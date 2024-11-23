def func(a: int, b: int) -> int:
    """return sum of two elements"""
    return a + b


print(func.__name__)  # имя функции
print(func.__dict__)  # пространство имён
print(func.__annotations__)  # аннотации
