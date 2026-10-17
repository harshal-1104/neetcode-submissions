
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        # Verify if the element at index 'i' matches 'x'
        if i != len(nums) and nums[i] == target:
            return i
        return -1