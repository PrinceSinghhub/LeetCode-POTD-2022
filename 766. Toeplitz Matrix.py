class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j in d and d[i - j] != matrix[i][j]:
                    return False
                else:
                    d[i - j] = matrix[i][j]

        return True