# Third Question: Deep sort
from collections.abc import Iterable as Iterable


def sort_input(listInput):
    # go over depth of different data structures
    # type of str or end of iteration
    if isinstance(listInput, str) or not isinstance(listInput, Iterable):
        return listInput
    # type of dictionary
    elif type(listInput) is dict:
        print('The type is: ' + str(type(listInput)))
        return sorted({key: sort_input(val) for key, val in listInput.items()}.items(), key=str)
    # type of set
    elif type(listInput) is set:
        print('The type is: ' + str(type(listInput)))
        # replace to str
        return set(sorted(listInput, key=lambda inp: str(inp)))
    # type of list
    elif type(listInput) is list:
        print('The type is: ' + str(type(listInput)))
        # replace to str
        return sorted([sort_input(val) for val in listInput], key=str)
    # type of tuple
    elif type(listInput) is tuple:
        print('The type is: ' + str(type(listInput)))
        # replace to str
        return tuple(sorted((sort_input(item) for item in listInput), key=str))


def print_sorted(lst: Iterable):
    return sort_input(lst)


if __name__ == '__main__':
    lst1 = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print_sorted(lst1)  # prints e.g. {"a":5, "b":[1,2,3,4], "c":6}
    print('For lst1 = {"a": 5, "c": 6, "b": [1, 3, 2, 4]} the answer is: ' + str(print_sorted(lst1)))
    print()
    lst2 = {'student1': ('bhanu', 10), 'student4': ('uma', 12),
            'student3': ('suma', 11), 'student2': ('ravi', 11),
            'student5': ('gayatri', 9)}
    print('For lst2 = {''student1'': (''bhanu'', 10), ''student4'': (''uma'', 12), ''student3'': (''suma'', 11),'
          ' ''student2'': (''ravi'', 11), ''student5'': (''gayatri'', 9)} the answer is: ' + str(print_sorted(lst2)))
    print()
    lst3 = [1, [1, 2, 3], 2, 0, 12]
    print('For lst3 = [1, [1, 2, 3], 2, 0, 12] ' + str(print_sorted(lst3)))
    lst4 = {5: 5, 'c': 6, 'b': [1, 3, 2, 4]}
    print('For lst4 = {(5): 5, (4): 6, (4): [1, 3, 2, 4]} the answer is: '
          + str(print_sorted(lst4)))
    print()
    set1 = {'Apples', ('Bananas', 'Oranges')}
    print('For set1 = {''Apples'', (''Bananas'', ''Oranges'')} the answer is: : ' + str(print_sorted(set1)))
