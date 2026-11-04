class Solution:
    def reverse(self, x: int) -> int:
        isNegative = True if x < 0 else False
        x= abs(x)
        highest, lowest, res = (1 << 31) - 1, -(1 << 31), 0
        while x > 0:
            digit = x % 10
            if (res > highest / 10) or (res < lowest / 10):
                return 0
            elif (res == highest / 10 and digit > highest % 10) or (res == lowest / 10 and digit < lowest % 10):
                return 0
            else:
                res = (res * 10) + digit
            x = x // 10
        return -(res) if isNegative else res