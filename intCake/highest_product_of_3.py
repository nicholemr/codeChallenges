def highest_product_of_3(list_of_ints):
    # Calculate the highest product of three numbers
    if len(list_of_ints) < 3:
        return 'list no long enougth'

    mult = list_of_ints[0]*list_of_ints[1]

    if mult > 0:
        highest_mult = mult
        lowest_neg_mult = 1
    else:
        lowest_neg_mult = mult
        highest_mult = 1

    print(highest_mult, lowest_neg_mult)
    res = None
    for i in range(2, len(list_of_ints)):

        # multiply current number * other two nums to give highest result

        mult = list_of_ints[i]*list_of_ints[i-1]

        # updates mult:
        if mult < 0:
            if not lowest_neg_mult:
                lowest_neg_mult = mult
            elif mult < lowest_neg_mult:
                lowest_neg_mult = mult
        else:
            if not highest_mult:
                highest_mult = mult
            elif mult > highest_mult:
                highest_mult = mult

    print(highest_mult, lowest_neg_mult)


l = [-10, 1, 3, 2, -10]
print(highest_product_of_3(l))
