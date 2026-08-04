class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        residuals = dict()
        
        for i,n in enumerate(nums): 
            resd = target-n
            if n in residuals:
                return [residuals[n],i]
            residuals[resd] = i
        