class Solution:
    def productExceptSelf(self, nums):
        drag_f = [1]
        drag_b = 1
        for i in range(len(nums)-1):
            drag_f.append(drag_f[-1]*nums[i])

        i = len(nums)-1
        res = []
        while i >= 0:
            res.append(drag_f[i]*drag_b)
            drag_b = nums[i]*drag_b
            i -= 1

        i = len(nums)-1
        resf = []
        while i >= 0:
            resf.append(res[i])
            i -= 1
        return resf


sol = Solution()
n = [1, 2, 3, 4, 5]
sol.productExceptSelf(n)
