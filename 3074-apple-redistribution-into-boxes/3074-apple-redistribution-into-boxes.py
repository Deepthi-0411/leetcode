class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        cnt = 0
        for c in capacity:
            total -= c
            cnt += 1
            if total <= 0:
                return cnt
        
        