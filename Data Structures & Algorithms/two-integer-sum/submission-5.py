class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        residuals = {}
        solution = []
        
        for i, n in enumerate(nums):
            if n in residuals:
                solution.append(residuals[n])
                solution.append(i)
                return solution
            residuals[target-n] = i

        return None