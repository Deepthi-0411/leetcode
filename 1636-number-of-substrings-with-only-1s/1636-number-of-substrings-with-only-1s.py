class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        ans = streak = 0
        for c in s:
            if c == '1':
                streak += 1
                ans = (ans + streak) % mod
            else:
                streak = 0
        return ans

        