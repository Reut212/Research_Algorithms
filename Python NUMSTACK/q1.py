import numpy as np


def Linear_Equations():
    i = 0
    save_vars = []
    vars_inp = input("Please insert number of variables: ")
    vars = int(vars_inp)
    print("Please insert " + vars_inp + " variables")

    for i in vars_inp:
        save_vars[i] = input("X" + i + " = ")
    A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
    B = np.array([25, -10, -4])
    X2 = np.linalg.solve(A, B)
    # print(X2)
    x1 = X2.item(0)
    x2 = X2.item(1)
    x3 = X2.item(2)
    print("X1 = ", x1)
    print("X2 = ", x2)
    print("X3 = ", x3)


if __name__ == '__main__':
    Linear_Equations()
