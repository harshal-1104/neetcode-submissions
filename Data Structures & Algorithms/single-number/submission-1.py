class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        runningXOR = nums[0] ^ nums[1]
        for i in range(2,len(nums)):
            runningXOR = runningXOR ^ nums[i]
        return runningXOR