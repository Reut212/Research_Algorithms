# First Question: Safe Call
def f(x: int, y: float, z):
    # sum all types together
    return x + y + z


# this function is divided to three cases:
# 1. no input of args and kwargs - return 'Not a valid input'
# 2. input of args (and kwargs)
# 3. no input of args but there is an input for kwargs
def safe_call(func, *args, **kwargs):
    if not args and not kwargs:
        return print('Not a valid input')
    argument = []
    arg1 = arg2 = arg3 = 0
    if args:
        print("arg:", args)
        print("kwarg:", kwargs)
        if len(args) == 1:
            arg1 = args[0]
            argument.append(arg1)
        if len(args) == 2:
            arg1 = args[0]
            arg2 = args[1]
            argument.append(arg1)
            argument.append(arg2)
        if len(args) > 2:
            arg1 = args[0]
            arg2 = args[1]
            arg3 = args[2]
            argument.append(arg1)
            argument.append(arg2)
            argument.append(arg3)
        print()
        print('Only Args Arguments: ', argument)
        print()
        print("First argument: ", arg1)
        print("Second argument: ", arg2)
        print("Third argument: ", arg3)
        if kwargs:
            for arg in kwargs.values():
                argument.append(arg)
        print()
        print('with Kwargs Arguments: ', argument)
        print()
    elif not args:
        if kwargs:
            for arg in kwargs.values():
                argument.append(arg)
            print()
            print('Only kwargs Arguments: ', argument)
            print()

            if len(argument) == 1:
                arg1 = argument[0]
                print("First argument: ", arg1)
            if len(argument) == 2:
                arg1 = argument[0]
                arg2 = argument[1]
                print("First argument: ", arg1)
                print("Second argument: ", arg2)
            if len(argument) > 2:
                arg1 = argument[0]
                arg2 = argument[1]
                arg3 = argument[2]
                print("First argument: ", arg1)
                print("Second argument: ", arg2)
                print("Third argument: ", arg3)
    else:
        return print('Not a valid input')
    try:
        print('You chose x = ' + str(arg1) + ', y = ' + str(arg2) + ' and z = ' + str(arg3))
        # raise an exception if x is not type of integer and y is not type of float
        integer_x = int(arg1)
        float_y = float(arg2)
    except ValueError:
        print(
            'Please check your inputs. The first input x = ' + str(
                arg1) + ' must be integer and the second input y = ' +
            str(arg2) + ' must be float.')
    # after types check perform number sum
    else:
        sum_xyz = func(arg1, arg2, arg3)
        print('Sum of x, y and z is: ' + str(sum_xyz))
        return sum_xyz


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    safe_call(f, 'a')
    safe_call(f, "two", 3, 5, 6, a=1, b=2)
    safe_call(f, a=1, b=2)
    safe_call(f,)
    safe_call(f, 5, "abc", 3)
    safe_call(f, 5, 7.0, 3)
    safe_call(f, "abc", 2.1, 3)
    safe_call(f, " ", " ", 3)
