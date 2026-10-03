class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            res += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return res

    def twoSumSmaller(self, nums: List[int], startIndex: int, target: int) -> int:
        res = 0
        left = startIndex
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                res += right - left
                left += 1
            else:
                right -= 1

        return res

