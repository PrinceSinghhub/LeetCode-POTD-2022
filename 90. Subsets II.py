class Solution:
    def subsetsWithDup(self, nums):

        result = []

        def dfs(curr, nums):

            result.append(curr[:])

            if (len(nums) == 0):
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(curr + [nums[i]], nums[i + 1:])

        dfs([], sorted(nums))
        return result

ans = Solution()
nums = [1,2,2]
print(ans.subsetsWithDup(nums))