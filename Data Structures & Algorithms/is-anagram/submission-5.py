class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters = dict()

        for st in s:
            if st not in letters:
                letters[st] = 1
            elif st in letters:
                letters[st] += 1
            
        for tt in t:
            if tt not in letters:
                return False
            elif letters[tt] == 0:
                return False
            else:
                letters[tt] -= 1

        for lt in letters.values():
            if lt != 0:
                return False
            
        return True

    

