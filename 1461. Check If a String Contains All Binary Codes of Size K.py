class Solution:
    def hasAllCodes(self, s, k):
        combination = set()

        for i in range(len(s) - k + 1):
            combination.add(s[i:i + k])

        return len(combination) == 2 * k



ans = Solution()
s = "00110110"
k = 2
print(ans.hasAllCodes(s,k))