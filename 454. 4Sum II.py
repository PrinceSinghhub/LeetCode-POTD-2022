import collections
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):

        counter = collections.Counter()

        # a+b = -(c+d) basice approch
        for i in nums1:
            for j in nums2:
                counter[i+j]+=1
        print(counter)
        ans = 0

        for i in nums3:
            for j in nums4:
                ans+=counter[-(i+j)]
        print(counter)
        return ans

ans = Solution()
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(ans.fourSumCount(nums1,nums2,nums3,nums4))




