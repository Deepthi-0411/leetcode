class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_ind = nums.index(max_val)
        for x in range(len(nums)):
            if x != max_ind and max_val < 2 * nums[x]:
                return -1
        return max_ind
        