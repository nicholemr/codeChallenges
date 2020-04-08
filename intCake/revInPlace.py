def reverse(list_of_chars):
    i = len(list_of_chars)-1

    while i >= 0:
        end_char = list_of_chars[i]
        list_of_chars.append(end_char)
        list_of_chars.pop(i)
        i -= 1

    print(list_of_chars)


l = ['c', 'a', 'r']
# reverse(l)

message = list('yummy is cake bundt chocolate')
# message = ['y', 'u', 'm', 'm', 'y', ' ', 'i', 's', ' ', 'c', 'a', 'k', 'e', ' ', 'b', 'u', 'n', 'd', 't', ' ', 'c', 'h', 'o', 'c', 'o', 'l', 'a', 't', 'e']
# print(message)


def reverse_words(message):
    rev_msg = rev_copy(message)

    l_i = len(message)-1
    while l_i >= 0:
        message.insert(0, rev_msg[l_i])
        message.pop()
        l_i -= 1


def rev_copy(arr):
    arr = "".join(arr).split(' ')
    l_i = 0
    r_i = len(arr)-1
    while l_i < r_i:
        arr[l_i], arr[r_i] = arr[r_i], arr[l_i]
        l_i += 1
        r_i -= 1
    # print(list((" ".join(arr))))
    return list((" ".join(arr)))


reverse_words(message)
# print(message)
expected = list('chocolate bundt cake is yummy')
print(expected)
print(expected == message)
