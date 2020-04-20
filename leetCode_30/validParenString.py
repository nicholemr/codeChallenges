class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        for char in s:
            if char == '(' or char == '*':
                stack.append(char)
            elif char == ')':
                if '(' in stack:
                    for i, item in enumerate(stack):
                        if item == '(':
                            stack.pop(i)
                            break
                elif '*' in stack:
                    for i, item in enumerate(stack):
                        if item == '*':
                            stack.pop(i)
                            break
                else:
                    return False
        if '(' in stack:
            res = []
            for i in stack:
                if i == '(':
                    res.append(i)
                elif i == '*':
                    if res:
                        res.pop()
        else:
            return True

        if '(' in res:
            return False
        return True


s = "()"
s = '(*)'
s = '(*))'
s = "(*()"
# s = '((()*)))'
# s = '((*))'
sol = Solution()
print(sol.checkValidString(s))
