class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        already = set()

        for i in range(len(strs)):

            if strs[i] in already:
                continue

            sub = [strs[i]]
            already.add(strs[i])

            j = i+1
            while j < len(strs):
                if sorted(strs[i]) == sorted(strs[j]):
                    sub.append(strs[j])
                    already.add(strs[j])
                j+=1
            
            result.append(sub)
        
        return result
                


            

            


