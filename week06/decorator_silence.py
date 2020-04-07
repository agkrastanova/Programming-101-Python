def silence(fileName):
    def inner(func):
        def check_value(args):
            if args >= 50:
                with open(fileName, 'w') as f:
                    f.write("Calling {} raised an error - ValueError: 'Omg.'. ".format(func.__name__) +
                            "Provided argument: {}\n".format(args))
            return None
        return check_value
    return inner
