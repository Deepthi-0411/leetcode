class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0

        for i in res:
            if (i - 1) not in res:
                len = 0
                while (i + len) in res:
                    len +=1
                longest = max(len, longest)
        return longest
            
        