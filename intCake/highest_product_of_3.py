def highest_product_of_3(list_of_ints):
    # Calculate the highest product of three numbers
    if len(list_of_ints) < 3:
        return 'list no long enough'


def multiply(arr):
    return arr[0]*arr[1]*arr[2]


l = [-10, 1, 3, 2, -10]
print(highest_product_of_3(l))
