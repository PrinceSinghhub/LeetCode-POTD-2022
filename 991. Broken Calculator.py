class Solution:
    def brokenCalc(self,X,Y):
        ans = 0
        while X < Y:
            ans += 1
            if Y % 2: Y += 1
            else: Y //= 2
        return X - Y + ans

ans = Solution()
startValue = 3
target = 10
print(ans.brokenCalc(startValue,target))
