import doctest


class List(list):
    # constructor
    def __init__(self, lst):
        super().__init__(lst)

    """
    This is an implementation for set get and del items 
    For example,
    myList = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ])
    >> myList[0, 1, 3]
    66
    >> myList[2] = 3
    [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], 3]
    >>> myList[0]
    [[1, 2, 3, 33], [4, 5, 6, 66]]
    >>> myList[1, 2]
    Traceback (most recent call last):
    ...
    Exception: Out Of Range
    >>> del(myList[1])
    [[[1, 2, 3, 33], [4, 5, 6, 66]], 3]
    """

    def __getitem__(self, *args):
        items = args[-1]
        if items is None:
            return None
        try:
            if isinstance(items, tuple):  # multidimensional arr
                item = super().__getitem__(args[0][0])  # get the item in a row
                # print("First row is: ", item)
                for i in args[0][1:]:  # go over all the requested columns
                    item = item[i]
                    # print("Get the requested column: ", item)
                return item
            else:  # single arr
                item = super().__getitem__(args[0])
                for index in args[1:]:
                    item = item[index]
                return item
        except IndexError:
            return "Out of bounds"

    def __delitem__(self, *args):
        item_to_del = args[-1]
        if item_to_del is None:
            return None
        # print()
        # print("Requested delitem is: ", item_to_del)
        try:
            if isinstance(item_to_del, tuple):  # multidimensional arr
                item = super().__delitem__(args[0][0])  # set the item in a row
                # print("First row is: ", item)
                for delIndex in args[0][1:-1]:  # go over all the requested columns
                    item = item[delIndex]
                    # print("Get the requested column: ", item)
                return
            else:  # single arr
                super().__delitem__(args[0])
                return
        except IndexError:
            return "Out of bounds"

    def __setitem__(self, *args):
        item_to_set = args[-1]
        if item_to_set is None:
            return None
        print()
        # print("Requested set is: ", item_to_set)
        try:
            if isinstance(item_to_set, tuple):  # multidimensional arr
                item = super().__getitem__(args[0][0])  # set the item in a row
                # print("First row is: ", item)
                for index in args[0][1:-1]:  # go over all the requested columns
                    item = item[index]
                    # print("Get the requested column: ", item)
                return
            else:  # single arr
                super().__setitem__(args[0], item_to_set)
                return
        except IndexError:
            return "Out of bounds"


if __name__ == '__main__':
    print(doctest.testmod())
    # myList = List([
    #     [[1, 2, 3, 33], [4, 5, 6, 66]],
    #     [[7, 8, 9, 99], [10, 11, 12, 122]],
    #     [[13, 14, 15, 155], [16, 17, 18, 188]],
    # ])
    # # get from a multidimensional arr
    # print(myList[0, 1, 3])
    # # get from a single arr
    # print(myList[0])
    # # index error
    # print(myList[4])
    # myList[2] = 3
    # print(myList[0])
    # print(myList)
    # # myList[1] = [1, 2]
    # print(myList[None])
    # print(myList[1])
    # print(myList)
    # del (myList[1])
    # print(myList)
