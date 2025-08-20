class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i, n):
                 substr = s[i:j+1]
                 if substr == substr[::-1] and len(substr) > len(res):
                     res = substr
        
        return res