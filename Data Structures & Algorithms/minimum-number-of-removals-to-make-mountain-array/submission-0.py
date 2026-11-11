from bisect import bisect_left
from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def lis_lengths(arr: List[int]) -> List[int]:
            # tails[i] stores the smallest possible ending value
            # of an increasing subsequence of length i + 1.
            tails = []
            # LIS length ending at each array position.
            lengths = []

            for num in arr:
                # Find position for current number.
                pos = bisect_left(tails, num)

                if pos == len(tails):
                    # Extend the longest subsequence.
                    tails.append(num)
                else:
                    # Improve the tail of an existing length.
                    tails[pos] = num

                # Length of LIS ending at this element.
                lengths.append(pos + 1)

            return lengths

        n = len(nums)

        # Increasing subsequence lengths from left.
        left = lis_lengths(nums)

        # Increasing lengths on reversed array correspond
        # to decreasing subsequences starting from right.
        right = lis_lengths(nums[::-1])[::-1]

        longest = 0

        for i in range(n):
            # Both mountain sides must exist (strictly increasing and decreasing).
            if left[i] > 1 and right[i] > 1:
                longest = max(longest, left[i] + right[i] - 1)

        return n - longest