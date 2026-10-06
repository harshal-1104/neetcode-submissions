class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        for num in nums:
            if num-1 in num_set:
                continue
            current = num
            current_streak=1
            while(current+1) in num_set:
                current_streak += 1
                current += 1
            longest_streak = max(longest_streak,current_streak)
        
        return longest_streak
        