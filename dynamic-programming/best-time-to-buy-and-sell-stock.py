class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        best_buy = prices[0]
        for num in prices:
            res = max(res, num-best_buy)
            best_buy = min(best_buy, num)
        return res

        