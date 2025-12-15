class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = cur = 1
        for i in range(1, len(prices)):
            cur = cur + 1 if prices[i] == prices[i-1] - 1 else 1
            ans += cur
        return ans
        