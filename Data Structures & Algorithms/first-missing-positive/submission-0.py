class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

    # Place each value i at index i-1 using cyclic sort
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] to its correct position
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # Find the first position where the value doesn't match
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

    # All values 1..n are present
        return n + 1
        