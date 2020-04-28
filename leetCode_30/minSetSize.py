def minSetSize(arr):
    arr.sort()
    threshold = len(arr)/2
    counts = []
    count = 0
    current = arr[0]
    for item in arr:
        if item == current:
            count += 1
        else:
            counts.append(count)
            current = item
            count = 1
    counts.append(count)

    counts.sort(reverse=True)

    length = 0
    min_set = 0
    for c in counts:
        length += c
        min_set += 1
        if length >= threshold:
            break
    return min_set


a = [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
print(minSetSize(a))
