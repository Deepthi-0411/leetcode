class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        count = 0
        for word in text.split():
            if all(c not in broken_set for c in word):
                count += 1
        return count
        

        