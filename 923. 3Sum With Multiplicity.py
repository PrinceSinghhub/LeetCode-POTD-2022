import collections
class Solution:
    def threeSumMulti(self, A, target):
        ans = 0
        mod = (10**9 + 7)
        n = len(A)
        level = collections.defaultdict(int)
        for i in range(2, n):
            for j in range(i-1):
                level[A[j] + A[i-1]] += 1
            ans = ans + level[target - A[i]]
            ans = ans % mod
        return ans

ans = Solution()
arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
print(ans.threeSumMulti(arr,target))