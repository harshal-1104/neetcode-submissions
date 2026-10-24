import math, sys
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highestValue = 0
        for i in piles:
            if i > highestValue:
                highestValue = i

        left, right, result = 1, highestValue, sys.maxsize

        while left <= right:
            mid = (left + right) // 2
            summation = 0
            
            for i in piles:
                summation += math.ceil(i/mid)
            if summation <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result