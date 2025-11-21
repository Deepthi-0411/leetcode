class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            L = s.find(c)
            R = s.rfind(c)
            if L != -1 and R != -1 and L < R:
                ans += len(set(s[L+1:R]))
        return ans
        