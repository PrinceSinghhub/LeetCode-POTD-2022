class Solution:

    def isPalndrome(self, s, start, end):

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    def check(self, s):
        start = 0
        end = len(s) - 1

        while start <= end:

            if s[start] == s[end]:
                start += 1
                end -= 1

            else:

                if self.isPalndrome(s, start + 1, end):
                    return start

                if self.isPalndrome(s, start, end - 1):
                    return start

                return -1

        return -2

    def validPalindrome(self, s):

        idx = self.check(s)

        if idx == -1:
            return False
        else:
            return True

ans = Solution()
s = "abca"
print(ans.validPalindrome(s))