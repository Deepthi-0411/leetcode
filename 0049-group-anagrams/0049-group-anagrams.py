class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            t = ''.join(sorted(s))
            hash[t].append(s)
        return list(hash.values()) 
        
        