class Solution:
    def lastStoneWeight(self, stones) -> int:
        if len(stones) == 1:
            return stones[0]

        stones = self.merge_sort(stones)

        return self.lastStoneWeight([stones.pop() - stones.pop()] + stones)

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr

        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        return self.merge_arr(self.merge_sort(left), self.merge_sort(right))

    def merge_arr(self, left, right):
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left[0])
                left.pop(0)
            else:
                merged.append(right[0])
                right.pop(0)
        return merged + left + right


sol = Solution()
arr = [2, 7, 4, 1, 8, 1]
arr = [7, 6, 7, 6, 9]
print(sol.lastStoneWeight(arr))
