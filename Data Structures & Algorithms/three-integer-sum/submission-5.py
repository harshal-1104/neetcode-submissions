class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        present = False

        for i in range(len(nums)):
            if (i> 0 and nums[i]==nums[i-1]):
                 continue
            left=i+1
            right= len(nums)- 1 #finding the last index value

            while left<right:
                #if nums[left]== nums[left+1]:
                    #left +=1
                    
                if nums[i]+nums[left]+nums[right]==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    present=True
                    
                    while (left<right and nums[left] == nums[left+1] ):
                        left+=1
                    while(left<right and nums[right] == nums[right-1]):
                        right-=1
                       
                    left+=1
                    right-=1
                
                elif nums[left]+nums[right] > -nums[i]:
                    right -= 1
                else:
                    left +=1
                
        
        if present == False:
            return []
        return ans
        