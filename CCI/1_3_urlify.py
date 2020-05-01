def urlify(string, length):

    char_arr = [char for char in string]
    queue = []

    for i in range(length):
        if char_arr[i] == ' ':
            queue.append('%20')
            char_arr[i] = queue.pop(0)
        elif queue:
            queue.append(char_arr[i])
            char_arr[i] = queue.pop(0)

    return ''.join(char_arr)


s = 'Mr John Smith  '
l = 13

print(urlify(s, l))
