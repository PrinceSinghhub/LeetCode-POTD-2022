class Solution:
    def maximumUniqueSubarray(self, nums):
        seen=set() # track visited elements in the window
        res=i=tot=0
        for j in range(len(nums)):
            x=nums[j]

            while i < j and x in seen:
                seen.remove(nums[i])
                tot-=nums[i]
                i+=1
            tot+=x
            seen.add(x)
            res=max(res, tot)
        return res


ans = Solution()
nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
print(ans.maximumUniqueSubarray(nums))