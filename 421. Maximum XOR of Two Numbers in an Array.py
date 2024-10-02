class Solution:
    def findMaximumXOR(self, nums):

        # FinalAns = 0
        # for i in range(len(nums)):
        #     ans = 0
        #     for j in range (i+1,len(nums)):
        #
        #         XOR = nums[i]^nums[j]
        #         if XOR>ans:
        #             ans = XOR
        #     if ans > FinalAns:
        #         FinalAns = ans

        # optimize code
        ans = 0
        for i in range(31, -1, -1):
            prefixs = set([num >> i for num in nums])

            ans = ans<<1
            candidate = ans + 1

            for pre in prefixs:
                if candidate ^ pre in prefixs:
                    ans = candidate
                    break
        return ans



        # return FinalAns
ans = Solution()
nums = [14,70,53,83,49,91,36,80,92,51,66,70]
print(ans.findMaximumXOR(nums))


