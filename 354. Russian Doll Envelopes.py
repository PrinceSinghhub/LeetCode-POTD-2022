from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes):

        def lis(nums):
            # print(nums)
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
                # print(dp)
            return len(dp)

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        return lis([envelope[1] for envelope in envelopes])

ans = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(ans.maxEnvelopes(envelopes))