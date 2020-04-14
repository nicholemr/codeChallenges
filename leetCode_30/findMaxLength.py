# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Input:
# [0,0,1,0,0,0,1,1]
# Expected:
# 6


class Solution:
    def findMaxLength(self, nums):
        d = {}
        d[0] = d[1] = 0
        length = 0
        actual_length = 0

        for i, num in enumerate(nums):
            d[num] += 1
            length += 1
            if length % 2 == 0:
                if d[0] != d[1]:
                    length = 1
                    d[0] = d[1] = 0
                    d[num] += 1
                else:
                    actual_length = length

        return actual_length


sol = Solution()
input = [0, 1, 0, 1, 1, 0, 0]
input = [0, 0, 0, 1, 1, 1, 0]

print(sol.findMaxLength(input))
