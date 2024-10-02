class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # left side
            if nums[mid] > nums[left]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            # right side
            elif nums[mid] < nums[left]:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                left = left + 1

        return False

ans = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(ans.search(nums,target))