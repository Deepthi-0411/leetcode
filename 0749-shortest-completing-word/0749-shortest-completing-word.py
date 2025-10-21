class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        
        result = None
        for word in words:
            word_count = Counter(word.lower())
            if all(word_count[c] >= target[c] for c in target):
                if result is None or len(word) < len(result):
                    result = word
        return result