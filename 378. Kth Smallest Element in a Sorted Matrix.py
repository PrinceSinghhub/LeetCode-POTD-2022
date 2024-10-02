class Solution:
    def kthSmallest(self, matrix,k):
        mat = []
        for i in matrix:
            mat.extend(i)
        mat.sort()
        return mat[k - 1]


