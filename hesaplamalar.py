def toplama(x, y):
    return x + y


def cikarma(x, y):
    return x - y


def carpma(x, y):
    return x * y


def bolme(x, y):
    if y == 0:
        return None
    return x / y


print(toplama(2, 3))
print(cikarma(10, 4))
print(carpma(-2, 4))
print(bolme(5, 0))
print(bolme(0, 5))
print(bolme(-6, 3))
