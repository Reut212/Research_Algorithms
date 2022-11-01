# First Question: Deep sort
def print_sorted(inputX):
    print()
    print('The type is: ' + str(type(inputX)))
    if type(inputX) is dict:
        print('The type is: ' + str(type(inputX)))
        for i in sorted(inputX.items()):
            print(i, end=" ")
    # elif type(inputX) is tuple:
    #     sorted_tup = tuple(sorted(inputX))
    #     print('The type is: ' + str(type(inputX)))
    #     print(sorted_tup)


if __name__ == '__main__':
    x = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print_sorted(x)  # prints e.g. {"a":5, "b":[1,2,3,4], "c":6}
    # print()
    # y = {'student1': ('bhanu', 10), 'student4': ('uma', 12),
    #         'student3': ('suma', 11), 'student2': ('ravi', 11),
    #         'student5': ('gayatri', 9)}
    # print_sorted(y)
    # print()
    # z = {('bhanu', 10): 'student1',
    #     ('uma', 12): 'student4',
    #     ('suma', 11): 'student3',
    #     ('ravi', 11): 'student2',
    #     ('gayatri', 9): 'student5'}
