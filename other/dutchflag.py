from typing import List


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    i, smaller, larger = 0, 0, int(len(A)-1)
    middle = smaller + 1
    pivot = A[pivot_index]
    print(pivot)

    # sort smaller
    while smaller < larger:
        print(i, A[i])
        if A[i] < pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller += 1
        elif A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1
        i += 1
        print(A)

    return A

    # smaller, equal, larger = 0, 0, len(A)
    # pivot = A[pivot_index]
    # # Keep iterating as long as there is an unclassified element.,
    # while equal < larger:
    #     # A[equal] is the incoming unclassified element.
    #     if A[equal] < pivot:
    #         A[smaller], A[equal] = A[equal], A[smaller]
    #         smaller, equal = smaller + 1, equal + 1
    #     elif A[equal] == pivot:
    #         equal += 1
    #     else:  # A[equal] > pivot.
    #         larger -= 1
    #         A[equal], A[larger] = A[larger], A[equal]


pi = 8
a = [-3, 0, 1, -5, -1, 3, -5, 4, 2]

a = [0, 1, 1, 2]
pi = 2
print(a)
dutch_flag_partition(pi, a)
print(a)
