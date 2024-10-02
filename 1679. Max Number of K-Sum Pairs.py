from collections import defaultdict


class Solution:
    def maxOperations(self, nums,k):

        counter = defaultdict(int)

        count = 0
        for x in nums:
            comp = k - x
            if counter[comp] > 0:
                counter[comp] -= 1
                count += 1
            else:
                counter[x] += 1

        return count


ans = Solution()
nums = [1, 2, 3, 4]
k = 5
print(ans.maxOperations(nums,k))