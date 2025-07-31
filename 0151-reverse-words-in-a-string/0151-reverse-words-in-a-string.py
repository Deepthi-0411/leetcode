class Solution(object):
    def reverseWords(self, s):
            words = s.strip().split()
            return ' '.join(reversed(words))
        