class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n+1)]
        for num in range(n+1):
            mask = 1
            for i in range(10):
                if (num & (mask << i)):
                    res[num] += 1
        return res