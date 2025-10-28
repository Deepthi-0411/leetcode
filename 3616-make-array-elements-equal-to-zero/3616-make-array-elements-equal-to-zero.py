class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        ans = 0
        l = 0
        for x in nums:
            if x != 0:
                l += x
            else:
                if 2 * l == s:
                    ans += 2
                elif abs(2 * l - s) == 1:
                    ans += 1
        return ans
        