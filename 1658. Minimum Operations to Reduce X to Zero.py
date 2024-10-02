class Solution:
    def minOperations(self, nums, x):

        maxLen = 0
        total = 0
        windowStart = 0
        targetSum = sum(nums)

        # edge cases
        if targetSum < x: return -1
        if targetSum == x: return len(nums)

        # opposite of sliding window but still do sliding window
        # so instead of find continous subarray,
        # we need to find outer points that is not included in continous subarray
        k = targetSum - x  # this is for continous subarray

        for windowEnd in range(len(nums)):
            total += nums[windowEnd]

            while total > k:
                total -= nums[windowStart]
                windowStart += 1

            if total == k:
                maxLen = max(maxLen, windowEnd - windowStart + 1)

        if maxLen != 0:
            return len(nums) - maxLen
        else:
            return -1

ans = Solution()
arr = [3,2,20,1,1,3]
x = 10
print(ans.minOperations(arr,x))