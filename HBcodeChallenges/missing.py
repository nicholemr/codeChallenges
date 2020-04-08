"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    """

    listnum = []
    i = 1
    while i <= max_num:
        listnum.append(i)
        i += 1
    # listnum = [1,2,3,4,5,6,7,8,9,10]
    for num in nums:
        listnum[num-1] = 'y'
    # listnum = [y,y,y,y,y,y,y,8,y,y]

    for item in listnum:
        if type(item) == int:
            print(item)

    # num_d = {}
    # for num in nums:
    #     num_d[num] = 'y'

    # for item in listnum:
    #     if item not in num_d:
    #         print(item)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
