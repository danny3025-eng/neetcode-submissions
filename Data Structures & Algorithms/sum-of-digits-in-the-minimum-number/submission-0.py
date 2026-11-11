class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        n=min(nums);total=0
        while n:
            total+=n%10;n//=10
        return 1-total%2

