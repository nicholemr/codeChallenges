"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    # find center
    if nrows % 2 != 0:
        row, col = int(nrows/2), int(nrows/2)
        sum = garden[row][col]
        garden[row][col] = 0
    else:
        mid1 = int(nrows/2)

        row = mid1
        col = mid1
        maxnum = garden[row][col]
        if garden[mid1][mid1+1] > maxnum:
            col = mid1+1
        if garden[mid1+1][mid1] > maxnum:
            row = mid1+1
        if garden[mid1+1][mid1+1] > maxnum:
            row = mid1+1
            col = mid1+1
        maxnum = garden[row][col]
        garden[row][col] = 0

        sum = maxnum

    while True:
        print(garden)
        # print(row, col)

        maxnum = 0
        sleepcheck = 0
        newcol, newrow = col, row
        if col-1 >= 0 and garden[row][col-1] > maxnum:

            maxnum = garden[row][col-1]
            # print('w', maxnum)
            garden[row][col-1] = 0
            newcol = col - 1
            sleepcheck += 1
        if row-1 >= 0 and garden[row-1][col] > maxnum:

            maxnum = garden[row-1][col]
            # print('n', maxnum)
            garden[row-1][col] = 0
            newrow = row-1
            sleepcheck += 1
        if col+1 < ncols and garden[row][col+1] > maxnum:

            maxnum = garden[row][col+1]
            # print('e', maxnum)
            garden[row][col+1] = 0
            newcol = col+1
            sleepcheck += 1
        if row+1 < nrows and garden[row+1][col] > maxnum:

            maxnum = garden[row+1][col]
            # print('s', maxnum)
            garden[row+1][col] = 0
            newrow = row+1
            sleepcheck += 1

        sum = sum + maxnum

        col = newcol
        row = newrow

        if sleepcheck == 0:
            break

    return sum


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
