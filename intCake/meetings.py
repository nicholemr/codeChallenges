def merge_ranges(meetings):

    s = set()
    # Merge meeting ranges
    for j, meeting in enumerate(meetings):
        m = meetings[j]
        start = meetings[j][0]
        end = meetings[j][1]

        for i, n in enumerate(meetings):
            if m[0] <= n[0] <= m[1]:
                if n[1] > end:
                    end = n[1]
                else:
                    end = m[1]
                meetings[i] = (start, end)

            if m[0] <= n[1] <= m[1]:
                if n[0] < start:
                    start = n[0]
                else:
                    start = m[0]
                meetings[i] = (start, end)

        s.add((start, end))

        if len(s) == len(meetings):
            return list(s)

    s = merge_ranges(list(s))
    print(list(s))
    return list(s)


def merge_ranges_sorted(meetings):

    sorted_meetings = split_and_sort(meetings)
    print(sorted_meetings)
    merged = []
    s, e = sorted_meetings[0]

    for i, m in enumerate(sorted_meetings):
        if i == len(sorted_meetings)-1:
            merged.append((s, e))
            break

        if sorted_meetings[i+1][0] <= e:
            e = max(e, sorted_meetings[i+1][1])
        else:
            merged.append((s, e))
            s, e = sorted_meetings[i+1]

    print(merged)
    return merged


def split_and_sort(tup_arr):

    if len(tup_arr) == 1:
        return tup_arr

    mid = int(len(tup_arr)/2)
    left = tup_arr[:mid]
    right = tup_arr[mid:]

    return sort_(split_and_sort(left), split_and_sort(right))


def sort_(left, right):

    sorted_tups = []
    while left and right:
        if left[0][0] < right[0][0]:
            sorted_tups.append(left[0])
            left.pop(0)
        else:
            sorted_tups.append(right[0])
            right.pop(0)
    return sorted_tups + left + right


# m = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# m = [(1, 8), (2, 5)]
# m = [(1, 4), (2, 5), (5, 8)]
# m = [(1, 8), (1, 5)]
# m = [(5, 8), (1, 4), (6, 8)]
# m = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# m = [(1, 10), (7, 9), (3, 5), (2, 6)]
#    [(0, 1), (3, 8), (9, 12)]
m = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

# merge_ranges(m)
# print(split_and_sort(m))
merge_ranges_sorted(m)
