class Solution:
    def removePalindromeSub(self, s):
        if s == s[::-1]:
            return 1
        return 2

ans = Solution()
s = "ababa"
print(ans.removePalindromeSub(s))