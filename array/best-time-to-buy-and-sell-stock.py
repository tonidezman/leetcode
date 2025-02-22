class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        best_buy = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - best_buy
            res = max(res, profit)
            best_buy = min(best_buy, prices[i])
        return res

"""
[7,1,5,3,6,4]
 ^
   ^
"""