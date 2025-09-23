class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        while w > 0:
            if area % w == 0:
                return [area // w, w]
            w -= 1
        return [area, 1]
        