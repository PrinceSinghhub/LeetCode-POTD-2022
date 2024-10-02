class Solution:
    def removeDuplicates(self, nums):

        # bruteforce approch
        # ans = []
        # for i in nums:
        #     if i in ans:
        #         pass
        #     if i not in ans and nums.count(i)>1:
        #         ans.append(i)
        #         ans.append(i)
        #     if i not in ans and nums.count(i)<=1:
        #         ans.append(i)
        #
        # return ans

        # optimixe code inplacae swaping
        L = len(nums)
        left = 1
        for right in range(1,L):
            if nums[right]!=nums[left-1]:
                nums[left] = nums[right]
                left+=1
                continue

            if left-2>=0 and nums[right]==nums[left-2]:
                continue
            nums[left] = nums[right]
            left+=1
        return left



ans = Solution()
nums = [1,1,1,2,2,3]
print(ans.removeDuplicates(nums))