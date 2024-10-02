class Solution:
    def maxScore(self, cardPoints, k):
        dpArray = [0 for i in range(k + 1)]

        dpArray[0] = sum(cardPoints[:k])

        for i in range(1, k + 1):
            dpArray[i] = dpArray[i - 1] - cardPoints[k - i] + cardPoints[-i]
        return max(dpArray)

ans = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(ans.maxScore(cardPoints,k))