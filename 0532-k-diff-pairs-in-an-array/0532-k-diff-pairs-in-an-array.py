class Solution(object):
    def findPairs(self, nums, k):
        result = set()
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    result.add ((min(nums[i], nums[j]), max(nums[i], nums[j])))
        return len(result)


        
        