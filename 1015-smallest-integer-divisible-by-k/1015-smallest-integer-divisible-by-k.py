class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 1 % k
        length = 1

        while rem != 0:
            rem = (rem * 10 + 1) % k
            length += 1

        return length
