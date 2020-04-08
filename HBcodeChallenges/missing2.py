def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    """

# sort list
# iterate and find where there is a num difference of 2


def merge_sort(nums):
    print(nums)
    if not nums:
        return nums

    mid = int(len(nums)/2)
    left = nums[:mid]
    right = nums[mid:]

    return merge_sort(left)

    # return sort(merge_sort(left), merge_sort(right))

# [7,3],    [2,4]
# [7]    [3]
# []   [7]
# [7]
# [3,7]
# [2,3,4,7]


def sort(a, b):

    # [5, 6, 1]   [9, 10]
    sorted = []
    i = 0
    while a and b:
        if a[i] > b[i]:
            item = a.pop(i)
            sorted.append(item)
        else:
            item = b.pop(i)
            sorted.append(b[i])
    return sorted + a + b


num_list = [7, 3, 2, 4, 5, 6, 1, 9, 10]
merge_sort(num_list)

# missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
