class Solution:
    def checkValidString(self, s):
        s = list(s)
        ast = []
        stack = []

        for i, item in enumerate(s):
            if item == '*' or item == '(':
                stack.append(item)
            if item == ')':
                if '(' in stack:
                    stack = self.removechar(stack, '(')
                elif '*' in stack:
                    stack = self.removechar(stack, '*')
                else:
                    return False
        if '(' not in stack:
            return True
        print(stack)
        last_stack = []
        for item in stack:
            if item == '(':
                last_stack.append(item)
            elif item == '*':
                if '(' in last_stack:
                    last_stack.remove('(')

        if '(' not in last_stack:
            return True

        return False

    def removechar(self, arr, char):
        new_arr = []
        last_i = len(arr)-1

        for i in range(last_i, -1, -1):
            if arr[i] == char:
                arr.pop(i)
                break
        return arr


s = "()"
s = '(*)'
# s = '(*))'
# s = "(*()"
# s = '((()*)))'
# s = '((*))'
# s = "(((******))"
s = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"
sol = Solution()
print(sol.checkValidString(s))
