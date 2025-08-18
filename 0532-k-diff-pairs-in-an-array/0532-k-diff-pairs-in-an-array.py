from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        counter = Counter(nums)
        result = 0
    
        if k == 0:
            for num in counter:
                if counter[num] > 1:
                    result += 1
        else:
            for num in counter:
                if num + k in counter:
                    result += 1
        return result


        
        