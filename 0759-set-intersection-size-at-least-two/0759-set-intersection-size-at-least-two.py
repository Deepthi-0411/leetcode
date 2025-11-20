class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = []
       
        for l, r in intervals:
            count = 0
            if res:
                if res[-1] >= l:
                    count += 1
                if len(res) > 1 and res[-2] >= l:
                    count += 1

            need = 2 - count
            while need > 0:
                res.append(r - (need - 1))
                need -= 1
        return len(res)
        