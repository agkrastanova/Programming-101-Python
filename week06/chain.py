def chain(iter1, iter2):
    res = []

    for x in iter1:
        res.append(x)

    for x in iter2:
        res.append(x)

    return res


def chain2(iter1, iter2):
    res = []

    res.extend(iter1)
    res.extend(iter2)

    return res


def chain3(iter1, iter2):
    return [*iter1, *iter2]


def chain4(iter1, iter2):
    res = [*iter1, *iter2]

    for x in res:
        yield x


def chain5(iter1, iter2):
    for x in iter1:
        yield x

    for x in iter2:
        yield x


iter1 = range(4)
iter2 = range(4, 10)


result = chain(iter1, iter2)
result2 = chain2(iter1, iter2)
result3 = chain3(iter1, iter2)
result4 = chain4(iter1, iter2)
result5 = chain5(iter1, iter2)


print(result)
print(result2)
print(result3)
print(result4)
print(result5)


# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
