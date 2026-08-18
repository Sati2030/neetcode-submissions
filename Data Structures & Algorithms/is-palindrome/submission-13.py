class Solution:
    def isPalindrome(self, s: str) -> bool:
        endi = len(s)-1
        starti = 0
        count = 0

        if endi == starti:
            return True

        while endi >= starti:
            if not s[endi].isalnum():
                endi -= 1
                continue
            if not s[starti].isalnum():
                starti += 1
                continue
            if s[endi].lower() != s[starti].lower():
                return False
            endi -= 1
            starti += 1 
            count += 1

        return True

