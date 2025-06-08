class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = 0
        m = 1
        max_profit = 0
        while m < len(prices):
            cur_profit = prices[m]- prices[n]
            if prices[n] < prices[m]:
                max_profit = max(cur_profit, max_profit)
            else:
                n = m
            m += 1
        return max_profit

        
    