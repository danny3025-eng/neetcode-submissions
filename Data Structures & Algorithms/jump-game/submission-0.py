class Solution:
    def canJump(self, nums: List[int]) -> bool:
      # Defines a function to check if the last index is reachable from the start.
        goal = len(nums) - 1  # Sets the initial target (goal) to the last index of the list (index 4).

        # Loops backwards starting from the second-to-last index (3) down to 0, stepping by -1.
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:  # Checks if standing at index i allows you to reach or jump past the current goal.
                goal = i  # Moves the goalpost back to index i since it can reach the previous goal.

        return goal == 0  # Returns True if the goal made it all the way back to the start (index 0), else False.
        