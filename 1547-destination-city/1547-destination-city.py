class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = {a for a, b in paths}
        for a, b in paths:
            if b not in start_cities:
                return b
        