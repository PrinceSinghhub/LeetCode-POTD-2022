class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        existed = []  # index indicates row, value indicates column
        self.dfs(n, existed, res)
        return res

    def dfs(self, n, existed, res):

        curr_row = len(existed)

        if curr_row == n:
            res.append(self.draw(existed))
            return

        for col in range(n):
            if not self.isValid(existed, curr_row, col):
                continue
            existed.append(col)
            self.dfs(n, existed, res)
            existed.pop()

    def isValid(self, existed, row, col):
        for r, c in enumerate(existed):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True

    def draw(self, existed):
        n = len(existed)
        board = []
        for i in range(n):
            row = ['Q' if j == existed[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board