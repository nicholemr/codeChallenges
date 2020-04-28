def minAddToMakeValid_(s):
    # first pass to accumulate all remaining opened parens
    # if close parens doesnt find avail opened parens, append to close parens stack
    # result = add up elements on both stacks
    opened = []
    closed = []

    for char in s:
        if char == '(':
            opened.append(char)
        elif opened:
            opened.pop()
        else:
            closed.append(char)

    return len(opened)+len(closed)


def minAddToMakeValid(s):
    countopen = 0
    countclosed = 0
    for char in s:
        if char == '(':
            countopen += 1
        else:
            if countopen > 0:
                countopen -= 1
            else:
                countclosed += 1

    return countclosed+countopen


s = "()))(("

print(minAddToMakeValid(s))
