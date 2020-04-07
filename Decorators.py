from functools import wraps


print('Hello inside the functions')


def accepts(*args):
    type_of_args = type(args)
    print('v accepts')

    def decorator(func):
        @wraps(func)
        def check_arguments(*arguments):
            print('v check_arguments')
            for i in range(len(arguments)):
                if type(arguments[i]) is not type_of_args:
                    string = "Argumen {} of {} is not {}!".format(arguments[i + 1], func.__name__, type_of_args)
                    raise TypeError(string)
            return func(*arguments)
        return check_arguments
    return decorator


print('Hello inside the functions')


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


print(say_hello(4))
