class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(i, n):
                if i<j:
                    matrix[i][j] = matrix[i][j] ^ matrix[j][i]
                    matrix[j][i] = matrix[i][j] ^ matrix[j][i]
                    matrix[i][j] = matrix[i][j] ^ matrix[j][i]
        for i in range(m):
            matrix[i].reverse()     