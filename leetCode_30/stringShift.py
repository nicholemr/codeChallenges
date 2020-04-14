# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


class Solution:
    def stringShift(self, s: str, shift):

        for dir, amount in shift:
            if dir == 1:
                s = s[-amount:] + s[:-amount]
            else:
                s = s[amount:] + s[:amount]
            print(s)


sol = Solution()
s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
sol.stringShift(s, shift)
