class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        result = [] 
    
        def combinations(curr, start, target): 
            if target == 0: 
                result.append(curr)  
                return  
        
            for i in range(start, len(candidates)): 
                if i > start and candidates[i] == candidates[i-1]: 
                    continue  
                if candidates[i] > target: 
                    break 
                
                combinations(curr + [candidates[i]], i + 1, target - candidates[i])

        combinations([], 0, target) 
        return result