class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        k %= (m * n)

        flat = tuple(grid[i][j] for i in range(m) for j in range(n))
        flat = flat[-k:] + flat[:-k]

        return [[flat[i * n + j] for j in range(n)] for i in range(m)]

ans = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(ans.shiftGrid(grid,k))