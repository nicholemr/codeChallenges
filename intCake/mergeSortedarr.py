def merged_lists(ml, al):

    merged = []

    max_i = min(len(ml), len(al))
    i = 0

    while i < max_i:
        if ml[i] < al[i]:
            merged.append(ml[i])
            al.insert(0, 0)
        else:
            merged.append(al[i])
            ml.insert(0, 0)
        i += 1
        max_i = min(len(ml), len(al))

    merged = merged + ml[i:] + al[i:]

    return merged


def merge_lists(ml, al):
    merged = []
    while ml and al:

        if ml[0] < al[0]:
            merged.append(ml[0])
            ml.pop(0)
        else:
            merged.append(al[0])
            al.pop(0)

    return merged + ml + al


my_list = [3, 4, 6, 10, 11]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
