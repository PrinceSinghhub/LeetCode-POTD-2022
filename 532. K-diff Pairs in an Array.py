class Solution:
    def findPairs(self, nums, k):

        check = set()
        ans = set()

        for i in nums:

            if i-k in check:
                ans.add(i-k)
            if i+k in check:
                ans.add(i)
            check.add(i)

        return len(ans)

ans = Solution()
nums = [3,1,4,1,5]
k = 2
print(ans.findPairs(nums,k))
