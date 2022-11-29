import doctest
import itertools


def bounded_subsets(lst, c):
    """
    Receive list of positive numbers and another positive number c
    There is an implementation for a bounded_subsets that the sum is not greater than c.
    >>> for n in bounded_subsets([1, 2, 3], 4): print(n, end="")
    [][1][2][3][1, 2][1, 3]

    >>> for n in bounded_subsets(range(50, 150), 103): print(n, end="")
    [][50][51][52][53][54][55][56][57][58][59][60][61][62][63][64][65][66][67][68][69][70][71][72][73][74][75][76][77][78][79][80][81][82][83][84][85][86][87][88][89][90][91][92][93][94][95][96][97][98][99][100][101][102][103][50, 51][50, 52][50, 53]

    >>> for n in zip(range(5), bounded_subsets(range(100), 1000000000000)): print(n, end="")
    (0, [])(1, [0])(2, [1])(3, [2])(4, [3])
    """
    subset_list = []
    if c < 0 or len(lst) == 0:
        yield []
        return
    for i in range(len(lst) + 1):
        for comb in itertools.combinations(lst, i):
            if sum(comb) <= c and comb not in subset_list:
                subset_list.append(comb)
                yield list(comb)
            else:
                break


# sort generator - followed "https://stackoverflow.com/questions/37743368/how-to-sort-generator-type-in-python"
def bounded_subsets_sum_order(lst, c):
    """
    Receive list of positive numbers and another positive number c
    There is an implementation for a bounded_subsets that the sum is not greater than c and receive
    subsets in ascending order of their amount.
    >>> for n in bounded_subsets_sum_order(range(8, 20), 23): print(n, end="")
    [][8][9][10][11][12][13][14][15][16][17][8, 9][18][8, 10][19][8, 11][8, 12][8, 13][8, 14][8, 15]
    """
    return sorted(bounded_subsets(lst, c), key=sum)


if __name__ == '__main__':
    print(doctest.testmod())
    # for s in bounded_subsets_sum_order(range(8, 20), 23):
    #     print(s, end=" ")

    # for s in bounded_subsets_sum_order(range(50, 150), 103):
    #     print(s, end="")
    # for s in bounded_subsets([1, 2, 3], 4):
    #     print(s, end="")
    # for s in bounded_subsets(range(50, 150), 103):
    #     print(s, end="")
    # for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
    #     print(s, end="")
