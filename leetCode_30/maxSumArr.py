class Solution:
    def maxSubArray(self, nums) -> int:

        L = None
        cs = None

        for i, num in enumerate(nums):
            if i == 0:
                L, cs = num, num

            else:
                # restart cs if num is greater than cs+num
                if cs+num > num:
                    cs += num
                else:
                    cs = num

                if cs > L:
                    L = cs

        return L


sol = Solution()
# print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(sol.maxSubArray([-1]))
print(sol.maxSubArray([1, 2]))
