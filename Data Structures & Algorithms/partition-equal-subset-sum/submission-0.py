class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False


# def canPartition(nums):  # Define function to see if array can be split into two equal-sum subsets
#   if sum(nums) % 2:  # If the total sum is odd, it's impossible to split equally; return False
#     return False

#   dp = set()  # Initialize a set to store all possible subset sums we can form
#   dp.add(0)  # Start with a base subset sum of 0 (using no elements)
#   target = sum(
#       nums
#   ) // 2  # Each subset needs to equal half of the total sum (the target)

#   # Iterate backwards through the array indices from the last element down to 0
#   for i in range(len(nums) - 1, -1, -1):
#     nextDP = set()  # Create a new set for the next iteration of subset sums

#     for t in dp:  # Go through each existing possible subset sum 't' in dp
#       if (
#           t + nums[i]
#       ) == target:  # If adding the current number 'nums[i]' hits the target sum...
#         return True  # ...we found a valid partition, so return True

#       nextDP.add(t + nums[i])  # Option 1: include nums[i] in the subset
#       nextDP.add(t)  # Option 2: do not include nums[i] in the subset

#     dp = nextDP  # Update dp set with the new sums found in this step

#   return False  # If loop finishes without hitting the target, return False


# print(canPartition(nums))  # Call the function and print the result (True/False)