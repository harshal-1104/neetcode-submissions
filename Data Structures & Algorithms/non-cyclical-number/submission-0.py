class Solution:
    def findSquare(self, num:int):
        return num*num
    def isHappy(self, n: int, hashset = None) -> bool:
        if n == 1:
            return True
        if hashset == None:
            hashset = set()
        sum= 0
        while n > 0:
            sum += self.findSquare(n % 10)
            n = n // 10
        if sum in hashset:
            return False
        else:
            hashset.add(sum)
            return self.isHappy(sum, hashset)