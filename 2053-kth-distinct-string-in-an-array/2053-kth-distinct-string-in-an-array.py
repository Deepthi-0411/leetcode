class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for w in arr:
            freq[w] = freq.get(w, 0) + 1
        
        for w in arr:
            if freq[w] == 1:
                k -= 1
                if k == 0:
                    return w
        return ""
        