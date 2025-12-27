class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for a, b in zip(w1, w2):
                if pos[a] < pos[b]:
                    break
                if pos[a] > pos[b]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False
        return True
        