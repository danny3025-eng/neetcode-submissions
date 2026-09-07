import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/speed)

            if hours <= h:
                right = speed

            else:
                left = speed + 1
        return left
