class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        val = []
        for word in words:
            v = 0
            for i,c in enumerate(word):
                v = v | (1 << (ord(word[i]) - ord('a')))
            val.append(v)
        ret = 0
        for i in range(len(val)):
            for j in range(i+1, len(val), 1):
                if val[i] & val[j] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret

ans = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(ans.maxProduct(words))