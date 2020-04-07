def accepts(*args):
    type_of_args = args

    def decorator(func):
        def check_arguments(*arguments):
            for i in range(len(arguments)):
                if type(arguments[i]) is not type_of_args[i]:
                    string = "Argument {} of {} is not {}!".format(arguments[i], func.__name__, type_of_args[i].__name__)
                    raise TypeError(string)
            return func(*arguments)
        return check_arguments
    return decorator
