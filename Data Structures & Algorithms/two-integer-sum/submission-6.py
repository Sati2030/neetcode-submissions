class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        residuals = dict()
        
        for i,n in enumerate(nums): 
            resd = target-n
            if n in residuals:
                return [residuals[n],i]
            print(resd)
            residuals[resd] = i

        for r in residuals.keys():
            print(f"residual: {r}")
        