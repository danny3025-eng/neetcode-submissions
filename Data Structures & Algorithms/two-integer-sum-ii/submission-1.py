class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            currsum = nums[l] + nums[r]

            if currsum > target:
                r -= 1
            elif currsum < target:
                l += 1
            else:
                return [l+1, r+1]

        return []
    
        