class Solution:
    def bestClosingTime(self, customers: str) -> int:
        score = 0
        best = 0
        ans = 0

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > best:
                best = score
                ans = i + 1

        return ans