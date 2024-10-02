class Solution:
    # brueforce Approch
    # def fourSum(self, nums, target):
    #
    #     nums.sort()
    #     L = len(nums)
    #     ans = set()
    #     for i in range(L):
    #         for j in range(i + 1, L):
    #             for k in range(j + 1, L):
    #                 for l in range(k + 1, L):
    #                     if nums[i] + nums[j] + nums[k] + nums[l] == target:
    #                         ans.add((nums[i],nums[j],nums[k],nums[l]))
    #     return list(ans)

    # optimize Solution
    def fourSum(self, nums,target):
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right] + nums[j]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.add(tuple(sorted((nums[i], nums[left], nums[right], nums[j]))))

                        left += 1
                        right -= 1
        return list(ans)



ans = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(ans.fourSum(nums,target))