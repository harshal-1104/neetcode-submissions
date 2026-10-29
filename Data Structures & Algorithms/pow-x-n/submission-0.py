class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        is_negative = n < 0
        n = abs(n)
        if n % 2:
            res = self.myPow(x, n // 2)
            return (1/ (res * res * x)) if is_negative else (res * res * x)
        else:
            res = self.myPow(x, n // 2)
            return (1/ (res * res)) if is_negative else (res * res)