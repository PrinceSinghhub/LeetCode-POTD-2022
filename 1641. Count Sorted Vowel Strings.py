class Solution:
    def countVowelStrings(self, n):
        a = e = i = o = u = 1

        for _ in range(n - 1):
            a, e, i, o, u = a + e + i + o + u, e + i + o + u, i + o + u, o + u, u

        return a + e + i + o + u


ans = Solution()
n = 2
print(ans.countVowelStrings(n))