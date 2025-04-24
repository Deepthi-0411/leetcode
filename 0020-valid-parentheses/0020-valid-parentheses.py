class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []

        for x in s:
            if x not in hashmap:
                stack.append(x)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[x]:
                        return False
        return not stack

          
    
        