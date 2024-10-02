class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0]) # dimensions
        ans = [-1]*n
        for j in range(n):
            k = j
            for i in range(m):
                kk = k + grid[i][k]
                if not 0 <= kk < n or grid[i][k] * grid[i][kk] < 0: break
                k = kk
            else: ans[j] = k # no break
        return ans 