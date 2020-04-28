def luckBalance(k, contests):
    # pick the contests with the highest Luck value
    important = []
    total = 0
    for l, i in contests:
        if i == 1:
            important.append(l)
        else:
            total += l

    important.sort(reverse=True)

    return sum(important[:k]) + total - sum(important[k:])


n = 6
k = 3
c = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

print(luckBalance(k, c))
