class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        runningXOR = 0
        for i in range(1,len(nums)+1):
            runningXOR = runningXOR ^ i
        for i in nums:
            runningXOR = runningXOR ^ i
        return runningXOR