class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        rest = {}

        if len(s) != len(t):
            return False 

        for st in s:
            if st in rest:
                rest[st] += 1
                continue
            rest[st] = 1

        for tr in t:
            if tr not in rest or rest[tr] == 0:
                return False
            rest[tr] -= 1
        
        return True