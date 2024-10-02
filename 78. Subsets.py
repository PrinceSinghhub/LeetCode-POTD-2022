class Solution:
    def subsets(self, nums):
        N = len(nums)
        anss = []

        def ans(index, current):
            if index == N:
                anss.append(current[:])
                return
            ans(index + 1, current)
            current.append(nums[index])

            ans(index + 1, current)
            current.pop()

        ans(0, [])
        return anss

#         ans = [[]]

#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 ans.append(nums[i:j+1])
#         return ans


ans = Solution()
nums = [1,2,3]
print(ans.subsets(nums))
