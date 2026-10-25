class Solution:
    def hammingWeight(self, n: int) -> int:
        counter, mask = 0,1
        for i in range(32):
            if (n & (mask << i)):
                counter+= 1
        return counter
        