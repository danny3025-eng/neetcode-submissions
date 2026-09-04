class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sorted_nums = sorted(count, key=count.get, reverse=True)

        return sorted_nums[:k]
        