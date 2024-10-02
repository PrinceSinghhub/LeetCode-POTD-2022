class Solution:

    def findWinner(self,n):
        if n == 0:
            return False

        i = 1
        while (i * i) <= n:
            if self.findWinner(n - i * i)  != True:
                return True
            i += 1;

        return False

    def winnerSquareGame(self, n):

        return self.findWinner(n)

ans = Solution()
n = 99
print(ans.winnerSquareGame(n))