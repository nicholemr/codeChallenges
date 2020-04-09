def has_palindrome_permutation(the_string):

    # make dict with input str char's and their count
    odd_count = set()

    for char in the_string:
        if char in odd_count:
            odd_count.remove(char)
        else:
            odd_count.add(char)

    return len(odd_count) == 1


str = 'aabcbcd'

print(has_palindrome_permutation(str))
