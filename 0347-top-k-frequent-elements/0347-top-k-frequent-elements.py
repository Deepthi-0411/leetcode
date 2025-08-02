from collections import Counter 

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [item for item, _ in count.most_common(k)]
        
        