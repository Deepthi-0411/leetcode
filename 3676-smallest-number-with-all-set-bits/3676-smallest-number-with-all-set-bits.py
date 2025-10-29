class Solution:
    def smallestNumber(self, n: int) -> int:
        k = n.bit_length()
        ans = (1 << k) - 1
        if ans < n:
            ans = (1 << (k + 1)) - 1
        return ans
        