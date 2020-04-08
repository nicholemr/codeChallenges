class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        doubles = set()
        for num in nums:
            if num not in doubles:
                doubles.add(num)
            else:
                doubles.remove(num)
        return doubles[0]
