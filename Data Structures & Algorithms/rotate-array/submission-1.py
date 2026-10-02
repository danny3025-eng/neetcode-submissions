class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Optimization to handle cases where k is larger than the array length
        
        while k:
            tmp = nums[n - 1]  # Save the last element
            for i in range(n - 1, 0, -1):  # Shift elements to the right
                nums[i] = nums[i - 1]
            nums[0] = tmp  # Move the saved element to the front
            k -= 1  # Decrease the rotation counter

        