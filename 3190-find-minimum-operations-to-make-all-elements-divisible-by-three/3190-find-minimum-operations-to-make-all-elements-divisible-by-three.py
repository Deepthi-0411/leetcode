class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            r = x % 3
            if r != 0:
                total += min(r, 3 - r)
        return total

        