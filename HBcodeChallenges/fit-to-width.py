"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""


def fit_to_width(string, limit):
    """Print string within a character limit."""

    input_words = string.split()
    i = 0
    line_list = []
    new_str = str()

    for word in input_words:
        if i == 0:
            new_str = word
        elif len(new_str+word) < limit:
            new_str = new_str + ' ' + word
        else:
            line_list.append(new_str)
            new_str = word
        if i == (len(input_words)-1):
            line_list.append(new_str)
        i += 1

    for string in line_list:
        print(string)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
