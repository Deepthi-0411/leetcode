class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
         dp = [0, float('-inf'), float('-inf')]

         for x in nums:
             new = dp[:]  # copy
             for r in range(3):
                 nr = (r + x) % 3
                 new[nr] = max(new[nr], dp[r] + x)
             dp = new

         return dp[0]