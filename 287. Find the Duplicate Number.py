# another approch
class Solution1:
    def findDuplicate(self, nums):

        nums.sort()

        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                return nums[i]

        return -1



class Solution:
    def findDuplicate(self, nums):

        # brute force approch
        #         for i in nums:
        #             if nums.count(i)>1:
        #                 return i

        # optimize code
        # apply binary search

        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (right + left) / 2

            if sum(i <= mid for i in nums) > mid:
                left = left
                right = mid
            else:
                left = mid + 1
                right = right

        return right

ans = Solution1()
nums = [1,3,4,2,2]
print(ans.findDuplicate(nums))