# First Question: Safe Call
def f(x: int, y: float, z):
    # sum all types together
    return x + y + z


def safe_call(func, x: int, y: float, z: any):
    try:
        print('You chose x = ' + str(x) + ', y = ' + str(y) + ' and z = ' + str(z))
        # raise an exception if x is not type of integer and y is not type of float
        integer_x = int(x)
        float_y = float(y)
    except ValueError:
        print(
            'Please check your inputs. The first input x = ' + str(x) + ' must be integer and the second input y = ' +
            str(y) + ' must be float.')
    # after types check perform number sum
    else:
        sum_xyz = func(x, y, z)
        print('Sum of x, y and z is: ' + str(sum_xyz))
        return sum_xyz


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    safe_call(f, 10, 2, 3)
    safe_call(f, 5, "abc", 3)
    safe_call(f, 5, 7.0, 3)
    safe_call(f, "abc", 2.1, 3)
    safe_call(f, " ", " ", 3)
