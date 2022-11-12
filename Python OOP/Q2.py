# defining decorator function
def lastcall(func, _saveData={}):
    _saveData[func] = []

    def wrapper_function(*args, **kwargs):
        try:
            val_func = func(*args, **kwargs)
            if args in _saveData[func]:
                print("I already told you that the answer is " + str(val_func) + "!")
            else:
                _saveData[func].append(args)
                print(str(val_func))
        except TypeError:
            print("Please insert a valid parameters")
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
    power(2)
    power()
    power(2)
    # mul_dif(a=2.1, b=4)
    sum_numbers(3, 4)
    sum_numbers(2, 1)
    sum_numbers(3, 4)
