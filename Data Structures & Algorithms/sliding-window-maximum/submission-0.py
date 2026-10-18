from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right, result = 0, 0, []
        q = deque()
        
        while right < len(nums):
            while q and nums[q[-1]] < nums[right]: #always emptying the dequeue before entering max value in dequeue
                q.pop()
                
            q.append(right)
            
            if left > q[0]: # getting rid of leftmost(highest in current window) from dequeue
                q.popleft()
                
            if (right + 1) >= k:
                result.append(nums[q[0]])
                left += 1
            right += 1
                
        return result  
        