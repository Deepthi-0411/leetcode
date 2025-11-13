class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        n = len(s)
        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:
                if i == n - 1 or s[i + 1] == '1':
                    ans += ones
        return ans
        
        