import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate
