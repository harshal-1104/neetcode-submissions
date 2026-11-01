class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        left, top, right, bottom = 0, 0, cols - 1, rows - 1
        res = []
        
        while top <= bottom and left <= right:
            # 1. Traverse Top Row
            for l in range(left, right + 1):
                res.append(matrix[top][l])
            top += 1
            
            # 2. Traverse Right Column
            for t in range(top, bottom + 1):
                res.append(matrix[t][right])
            right -= 1
            
            # Safety check to avoid duplicate traversal in 1D rows/cols
            if top > bottom or left > right:
                break
            
            # 3. Traverse Bottom Row
            for r in range(right, left - 1, -1):
                res.append(matrix[bottom][r])
            bottom -= 1
            
            # 4. Traverse Left Column
            for b in range(bottom, top - 1, -1):
                res.append(matrix[b][left])
            left += 1
            
        return res