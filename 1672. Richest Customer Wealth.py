class Solution:
    def maximumWealth(self, accounts):

        ans = 0
        for i in accounts:
            if sum(i) > ans:
                ans = sum(i)
        return ans

ans = Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(ans.maximumWealth(accounts))