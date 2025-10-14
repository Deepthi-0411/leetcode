class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        pre = 0
        cur = 0
        mx = 0
        n = len(nums)
        
        for i in range(n):
            cur += 1
            if i == n - 1 or nums[i] >= nums[i + 1]:
                mx = max(mx, cur // 2, min(pre, cur))
                pre = cur
                cur = 0
        
        return mx >= k

        