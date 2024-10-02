class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        first_half, second_half = 0, sum(nums)
        num_first_half = 0
        ans, min_ind = 1e18, 1e18
        for i in range(len(nums)):
            first_half += nums[i]
            num_first_half += 1
            if i < len(nums) - 1:
                carry = abs((first_half // num_first_half) - ((second_half - first_half)//(len(nums) - i - 1)))
            else:
                carry = abs(first_half // num_first_half)
            if carry < ans:
                ans = carry
                min_ind = i
        return min_ind