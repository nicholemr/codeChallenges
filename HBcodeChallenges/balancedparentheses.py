"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    # left = 0
    # right = 0
    # for char in phrase:
    #     if char == '(':
    #         left += 1
    #     elif char == ')':
    #         right += 1
    # if left == right:
    #     return True
    # return False
    stack = []
    for char in phrase:
        if char == '(':
            stack.append(char)
        if char == ')':
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
