class Solution:
    def minimumLengthEncoding(self, words):

        words.sort(reverse=True)
        ans = ''
        for x in words:
            if x + '#' not in ans:
                ans += x + '#'
        return len(ans)

ans = Solution()

words = ["time", "me", "bell"]
print(ans.minimumLengthEncoding(words))