class Solution:
    def transpose(self, matrix):

        ans = []

        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])

            ans.append(temp)

        return ans

ans = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(ans.transpose(matrix))