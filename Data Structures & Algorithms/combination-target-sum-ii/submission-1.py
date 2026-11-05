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
# ========================
# def combinationsum2(candidates, target):
#     # Sort the input numbers so we can easily skip duplicates and break early when numbers get too large.
#     candidates.sort()
    
#     # Initialize an empty list to store all the unique combinations that sum up to the target.
#     result = [] 
    
#     # Define a helper function to perform a Depth-First Search (DFS) / Backtracking.
#     # 'curr' is the current combination, 'start' is the next available index, and 'target' is the remaining sum needed.
#     def combinations(curr, start, target):
#         # Base Case: If the remaining target is exactly 0, we found a valid combination.
#         if target == 0:
#             # Add a copy of the current valid combination to our final results list.
#             result.append(curr)
#             # Return to backtrack and explore other potential combinations.
#             return 
        
#         # Loop through the remaining candidate numbers starting from the 'start' index.
#         for i in range(start, len(candidates)):
#             # If the current number is the same as the previous number *within the same decision level*,
#             # skip it to avoid generating duplicate combinations in the final result.
#             if i > start and candidates[i] == candidates[i-1]:
#                 continue
            
#             # Optimization: Because the list is sorted, if the current number is strictly greater than 
#             # the remaining target, no subsequent numbers can fit either. We can stop the loop early.
#             if candidates[i] > target:
#                 break 
            
#             # Recursively call the helper function:
#             # 1. Add the current candidate to our combination list: 'curr + [candidates[i]]'
#             # 2. Move the index forward to 'i + 1' so we don't reuse the exact same element instance.
#             # 3. Reduce the target by the value of the number we just used: 'target - candidates[i]'
#             combinations(curr + [candidates[i]], i + 1, target - candidates[i])
            
#     # Simply invoke the helper function to populate the 'result' array
#     combinations([], 0, target)
    
#     # Return the final list containing all unique combination arrays.
#     return result