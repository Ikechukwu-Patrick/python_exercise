digits = list(range(1, 51))


def jumoke(p):
    return p ** 2


print(list(map(jumoke, digits)))


def check_even(number):
    return number % 2 == 0


print(list(filter(check_even, digits)))
print(list())
