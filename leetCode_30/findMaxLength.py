# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


class Solution:
    def findMaxLength(self, nums):
        count = 0
        maxcount = 0
        while len(nums) > 1:
            if nums[0:2] == [1, 0] or [0, 1]:
                count += 2
                nums = nums[2:]
            else:
                count = 0
            if count > maxcount:
                maxcount = count
        return maxcount


sol = Solution()
input = [0, 1, 0, 1, 1, 0, 0]
print(sol.findMaxLength(input))
