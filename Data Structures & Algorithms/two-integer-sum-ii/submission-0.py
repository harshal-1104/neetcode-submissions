class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers == []:
            return []

        left = 0
        right = len(numbers) - 1
        present = False

        while(left < right):
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                present = True
                return [left+1, right+1]
            elif current_sum < target:
                left += 1

            else:
                right -= 1

        if present == False: 
            return []
        