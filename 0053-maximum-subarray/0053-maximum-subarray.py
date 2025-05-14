class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = max_sum = nums[0] 
        for i in range (1,len(nums)):
            sum = max(nums[i], sum+nums[i])
            max_sum = max(max_sum,sum) 
        return max_sum