from functools import wraps


def decor(multiplier, *args, **kwargs):
    def decor_wrapper(func):
        @wraps(func)
        def wrapper(argument):
            print("BEFORE AAAA")
            func(argument * multiplier)
            print("AFTER AAAA")

        return wrapper

    return decor_wrapper


@decor(multiplier=2)
def screamer(word):
    """Screamer nice help"""
    print("AAAAAA {}".format(word))


#print(dir(screamer))
#print(help(screamer))

screamer("qwe")
