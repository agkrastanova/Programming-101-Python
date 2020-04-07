import time


def performance(fileName):
    def inner(func):
        def decorator():
            start = time.time()
            func()
            end = time.time()
            with open(fileName, 'a') as f:
                f.write("{} was called and took {:.2f} seconds to complete\n".format(func.__name__, (end - start)))
            return func()
        return decorator
    return inner
