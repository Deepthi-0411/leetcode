class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for a in range(1, n):
            for b in range(1, n):
                s = a*a + b*b
                c += int(int(s**0.5)**2 == s and int(s**0.5) <= n)
        return c