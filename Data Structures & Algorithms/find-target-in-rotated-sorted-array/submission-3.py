class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
        
        # Found the target
            if nums[mid] == target:
                return mid
        
        # 1. Find sorted half: LEFT half is sorted
            if nums[left] <= nums[mid]:
            # 2. Check target: Is it within the sorted left boundaries?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Keep left, discard right
                else:
                    left = mid + 1   # Keep right, discard left
                
        # 1. Find sorted half: RIGHT half is sorted
            else:
            # 2. Check target: Is it within the sorted right boundaries?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Keep right, discard left
                else:
                    right = mid - 1  # Keep left, discard right
                
        return -1
        