def is_first_come_first_served(takeout, dinein, served):

    # Check if we're serving orders first-come, first-served
    check = []

    while takeout and dinein:
        if takeout[0] < dinein[0]:
            check.append(takeout[0])
            takeout.pop(0)
        else:
            check.append(dinein[0])
            dinein.pop(0)
    check += takeout + dinein
    # print(check)

    return check == served


t, d, s = [1, 5], [2, 3, 6], [1, 6, 3, 5]

res = is_first_come_first_served(t, d, s)
print(res)
