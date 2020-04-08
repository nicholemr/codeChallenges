import timeit


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start = timeit.default_timer()

        i = 0
        zeroes = []
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeroes.append(0)

            else:
                i += 1

        nums.extend(zeroes)

        stop = timeit.default_timer()
        print('Time: ', round((stop - start)*1000, 4))


# [0, 1, 0, 3, 12]
#  i = 0
#  [1,0,3,12,0], i=0
# [0, 1, 0, 3, 12]

sol = Solution()
# lst = [0, 0, 0, 3, 12]
lst = [0, 1, 0, 3, 12]
sol.moveZeroes(lst)
print(lst)
