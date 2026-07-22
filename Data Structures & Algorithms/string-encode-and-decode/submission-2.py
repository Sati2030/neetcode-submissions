class Solution:

    def encode(self, strs: List[str]) -> str:   
        result = ""
        for strg in strs:
            stlen = len(strg)
            result += chr(stlen)
            result += strg
        return result
        
            
    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []

        result = []
        count = ord(s[0])
        temp = ""

        for c in s[1:]:
            if count == 0:
                result.append(temp)
                temp = ""
                count = ord(c)
            else:
                temp += c
                count -= 1
        result.append(temp)

        return result
