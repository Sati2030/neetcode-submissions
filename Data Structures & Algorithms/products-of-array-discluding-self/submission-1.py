class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        running = 1
        for i in range(len(nums)):
            if i == 0:
                result.append(1)
                continue
            running *= nums[i-1]
            result.append(running)

        running = nums[len(nums) - 1]

        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                result[i] *= 1
                continue
            result[i] *= running
            running *= nums[i]

        return result
        
            

            

            
        


