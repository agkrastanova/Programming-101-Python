def func(x):
    return x * 2


def deep_apply(func, data):
    for keys in data.keys():
        if type(data[keys]) is dict:
            deep_apply(func, data[keys])
        else:
            data[keys] = func(data[keys])

    return data
