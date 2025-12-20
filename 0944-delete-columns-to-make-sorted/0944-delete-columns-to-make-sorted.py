class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for c in zip(*strs):
            if list(c) != sorted(c):
                cnt += 1
        return cnt
        