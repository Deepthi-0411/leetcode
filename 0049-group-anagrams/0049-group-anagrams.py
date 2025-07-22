class Solution(object):
    def groupAnagrams(self, strs):
        hash = defaultdict(list)
        for s in strs:
            t = ''.join(sorted(s))
            hash[t].append(s)
        return list(hash.values()) 
        