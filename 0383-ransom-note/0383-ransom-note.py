class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for ch, cnt in ransom_count.items():
            if magazine_count[ch] < cnt:
                return False
        return True
        
        