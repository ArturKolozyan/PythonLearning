def recursion(a):
    if a < 0:
        return print(-1)
    if a == 0:
        return print(0)
    print(a)
    return recursion(a - 1)


recursion(-5)
recursion(5)
