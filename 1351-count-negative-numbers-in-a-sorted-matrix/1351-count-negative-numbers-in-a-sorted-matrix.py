class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        i, j = r - 1, 0
        cnt = 0

        while i >= 0 and j < c:
            if grid[i][j] < 0:
                cnt += c - j
                i -= 1
            else:
                j += 1
        return cnt
        

        

        