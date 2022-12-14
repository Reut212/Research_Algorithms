import doctest


# defining decorator function
def lastcall(func, _saveData={}):
    """
    This is an implementation for a decorator that remember if the last input identical to the previous input.

    The program supplies two function, lastcall(func, _saveData={}) - a decorator and rapper_function(*args, **kwargs).

    For example,
    >>> power(x=2)
    4
    >>> power(2)
    'I already told you that the answer is 4!'
    """
    _saveData[func] = []

    def wrapper_function(*args, **kwargs):
        try:
            val_func = func(*args, **kwargs)
            if len(kwargs.values()) != 0:
                if tuple(kwargs.values()) not in _saveData[func]:
                    _saveData[func].append(tuple(kwargs.values()))
                    return val_func
                else:
                    return "I already told you that the answer is " + str(val_func) + "!"
            elif len(args) != 0:
                if args not in _saveData[func]:
                    _saveData[func].append(args)
                    return val_func
                else:
                    return "I already told you that the answer is " + str(val_func) + "!"
            else:
                return "Please insert a valid parameters"
        except TypeError:
            return "Please insert a valid parameters"

    return wrapper_function


@lastcall
def div_same(x):
    return x / x


@lastcall
def div_dif(x, y):
    return x / y


@lastcall
def mul_same(x):
    return x * x


@lastcall
def mul_dif(x, y):
    return x * y


@lastcall
def sum_numbers(x, y):
    return x + y


@lastcall
def power(x):
    return x ** 2


if __name__ == '__main__':
    print(doctest.testmod())
    # power(x=2)
    # power()
    # power(2)
    # mul_dif(x=2.1, y=4)
    # mul_dif(2.1, 4)
    # sum_numbers(3, 4)
    # sum_numbers(2, 1)
    # sum_numbers(3, 4)
