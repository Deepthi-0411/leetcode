class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        c = Counter(arr)
        ans = -1
        for x in c:
            if c[x] == x:
                ans = max(ans, x)
        return ans
        