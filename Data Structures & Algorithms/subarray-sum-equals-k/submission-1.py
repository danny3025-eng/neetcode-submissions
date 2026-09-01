class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cursum = 0
        prefixsums = {0 : 1}

        for num in nums:
            cursum += num
            diff = cursum - k

            res += prefixsums.get(diff, 0)
            prefixsums[cursum] = 1 + prefixsums.get(cursum, 0)

        return res
        