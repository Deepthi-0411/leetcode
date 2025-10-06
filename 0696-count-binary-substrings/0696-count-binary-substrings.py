class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        res += min(prev, curr)
        return res

        