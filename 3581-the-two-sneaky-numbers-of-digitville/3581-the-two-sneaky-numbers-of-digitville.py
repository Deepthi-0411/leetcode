class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [num for num, count in freq.items() if count == 2]
        