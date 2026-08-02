from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the current subarray is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            # Left half is sorted, so minimum must be in the right half
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Minimum is in the left half (including mid)
                r = m - 1

        return res
        
            
        
        