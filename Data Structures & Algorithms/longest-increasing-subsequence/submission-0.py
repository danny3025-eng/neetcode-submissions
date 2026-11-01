class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # tails[i] = smallest tail element for increasing subsequence of length i+1
        tails = []

        for num in nums:
            # Binary search for the leftmost position where tails[pos] >= num
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # Replace or append
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)