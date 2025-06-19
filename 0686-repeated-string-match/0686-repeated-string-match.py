class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = 1
        repeated_a = a

        while len(repeated_a) < len(b):
            repeated_a += a
            repeated += 1

        if b in repeated_a:
            return repeated
        if b in repeated_a + a:
            return repeated + 1

        return - 1
      
        