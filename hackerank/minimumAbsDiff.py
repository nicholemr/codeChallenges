def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = None

    for i, num in enumerate(arr):

        if i == len(arr)-1:
            break

        diff = abs(num - arr[i+1])
        if not min_diff:
            min_diff = diff
        else:
            min_diff = min(diff, min_diff)

    return min_diff


# a = [1, 71, 17, -3, 68]
a = [3, -7, 0]
a = [1, -3, 71, 68, 17]
print(minimumAbsoluteDifference(a))
