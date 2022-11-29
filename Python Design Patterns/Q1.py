import itertools


def bounded_subsets(lst, c):
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
    return sorted(bounded_subsets(lst, c), key=sum)


if __name__ == '__main__':
    for s in bounded_subsets_sum_order(range(50, 150), 103):
        print(s, end=" ")
    # for s in bounded_subsets([1, 2, 3], 4):
    #     print(s)
    # for s in bounded_subsets(range(50, 150), 103):
    #     print(s)
    # for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
    #     print(s)
