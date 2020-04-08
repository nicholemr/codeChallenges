class Solution:
    def maxProfit(self, prices):

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        print(profit)
        return profit


sol = Solution()
# p = [7, 1, 5, 3, 6, 4]
# p = [1, 2, 3, 4, 5]
# p = [7, 6, 4, 3, 1]
p = [3, 2, 6, 5, 0, 3]
sol.maxProfit(p)
