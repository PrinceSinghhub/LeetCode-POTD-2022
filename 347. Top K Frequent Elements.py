from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        mydic = Counter(nums)
        most = mydic.most_common(k)

        print(mydic)
        print(most)
        return [i for i, val in most]


ans = Solution()
print(ans.topKFrequent([1,1,1,2,2,3],2))