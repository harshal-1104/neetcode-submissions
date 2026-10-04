class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        
        prefix = []
        prefix.append(1)

        for i in range(1,len(nums)):
            prefix.append(nums[i-1] * prefix[i-1])

        suffix = [1 for _ in range(len(nums))]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        ans = [prefix[i]*suffix[i] for i in range(len(nums))]

        return ans
        