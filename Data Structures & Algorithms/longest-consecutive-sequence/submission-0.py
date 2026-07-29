class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n-1 not in nums_set:
                temp = n+1
                temp_len = 1
                while temp in nums_set:
                    temp_len += 1
                    temp += 1
                if temp_len > longest:
                    longest = temp_len

        return longest

                    
        
                
            