class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        ans = cur = 0
        for c in s:
            cur = cur + 1 if c == '1' else 0
            ans = (ans + cur) % mod
        return ans
        

        