class Solution:
    def nextPermutation(self, nums):

        i = j = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        while nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        nums[i:] = nums[len(nums) - 1:i - 1:-1]

        return nums

ans = Solution()
nums = [1, 2, 3]
print(ans.nextPermutation(nums))