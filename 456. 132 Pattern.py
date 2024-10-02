class Solution:
    def find132pattern(self, nums):

        height = float('-inf')

        stack = []

        for i in range(len(nums) - 1, -1, -1):

            if nums[i] < height:
                return True

            while len(stack) != 0 and nums[i] > stack[-1]:
                height = stack.pop()

            stack.append(nums[i])

        return False

ans = Solution()
nums = [1, 2, 3, 4]
print(ans.find132pattern(nums))