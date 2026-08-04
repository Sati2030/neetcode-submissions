class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        coll = set()

        for n in nums:
            if n in coll:
                return True
            else:
                coll.add(n)

        return False

    


