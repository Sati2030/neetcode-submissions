class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        table = set()

        for n in nums:
            if n in table:
                return True
            else:
                table.add(n)
        
        return False

