class Solution:
    def maxAreaOfIsland(self, grid):

        def getArea(r, c, area):

            if r >= rows or r < 0 or c >= cols or c < 0:
                return 0

            if grid[r][c] == 0: return 0

            grid[r][c] = 0
            area = 1 + getArea(r - 1, c, area) + getArea(r + 1, c, area) + getArea(r, c + 1, area) + getArea(r, c - 1,
                                                                                                             area)
            return area

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, getArea(r, c, 0))
        return maxArea

ans = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(ans.maxAreaOfIsland(grid))
