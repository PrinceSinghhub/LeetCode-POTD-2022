class Solution:
    def gameOfLife(self, board):

        m, n = len(board), len(board[0])
        for i, j in product(range(m), range(n)):
            cnt = 0
            for di, dj in product(range(-1, 2), repeat=2):
                if di != 0 or dj != 0:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n:
                        cnt += board[ii][jj] & 1
            if cnt == 3 or (cnt == 2 and board[i][j] & 1):
                board[i][j] |= 2
        # print(board)
        for i, j in product(range(m), range(n)):
            board[i][j] >>= 1

