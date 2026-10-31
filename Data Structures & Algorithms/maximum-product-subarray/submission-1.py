class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the global maximum result with the first number in the list
        res = nums[0]
        
        # Track the current minimum and maximum products ending at the current position
        # Initialized to 1 because 1 is the multiplicative identity
        curMin, curMax = 1, 1 

        for num in nums:
            # Store the previous curMax before it gets updated, 
            # as it is needed to calculate the new curMin
            tmp = curMax * num
            
            # Update curMax by finding the maximum among:
            # 1. Multiplying the current number with the previous curMax
            # 2. Multiplying the current number with the previous curMin (handles negative * negative)
            # 3. Starting a brand new subarray from the current number itself
            curMax = max(num * curMax, num * curMin, num)
            
            # Update curMin by finding the minimum among:
            # 1. The pre-calculated tmp (previous curMax * num)
            # 2. Multiplying the current number with the previous curMin
            # 3. Starting a brand new subarray from the current number itself
            curMin = min(tmp, num * curMin, num)
            
            # Update the global maximum result if the newly found curMax is larger
            res = max(res, curMax)
            
        # Return the largest product found across all subarrays
        return res