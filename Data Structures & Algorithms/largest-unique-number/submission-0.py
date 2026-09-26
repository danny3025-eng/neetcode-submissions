class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        frequency_map = Counter(nums)

        return max((num for num, freq in frequency_map.items() if freq == 1), default=-1)