class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev = 0
        
        for l in logs:
            f, typ, t = l.split(":")
            f = int(f)
            t = int(t)
            
            if typ == "start":
                if stack:
                    res[stack[-1]] += t - prev
                stack.append(f)
                prev = t
            else:
                res[stack.pop()] += t - prev + 1
                prev = t + 1
        
        return res
        