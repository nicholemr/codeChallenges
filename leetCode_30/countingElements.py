class Solution:
    def countElements(self, arr):
        el_count = set()
        res = 0

        # for el in arr:
        #     el_count.add(el)

        [el_count.add(el) for el in arr]

        for el in arr:
            if el+1 in el_count:
                res += 1

        print(res)
        return res


sol = Solution()

# a = [1, 2, 3]
# a = [1, 1, 3, 3, 5, 5, 7, 7]
# -> 0
# a = [1, 3, 2, 3, 5, 0]
a = [1, 1, 2, 2]

sol.countElements(a)
