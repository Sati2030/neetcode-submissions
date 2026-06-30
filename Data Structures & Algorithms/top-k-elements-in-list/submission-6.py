class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencyDict = [[] for i in range(len(nums) + 1)]
        count = {}
        current = nums[0]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n , c in count.items():
            frequencyDict[c].append(n)

        result = []
        k_count = 0
        for i in reversed(range(len(frequencyDict))):
            if not frequencyDict[i-1]:
                continue
            for j in frequencyDict[i-1]:
                result.append(j)
                k_count += 1
                print(k_count)
                if k_count == k:
                    return result

        return result


        


        