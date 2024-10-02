from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s, words):
        store_words = defaultdict(list)

        print(store_words)

        for word in words:
            store_words[word[0]].append(word)

        print(store_words)

        cnt = 0
        for ch in s:

            arr = list(store_words[ch])
            store_words[ch] = []
            while arr:
                word = arr.pop()[1:]

                if len(word) == 0:
                    cnt += 1
                else:
                    store_words[word[0]].append(word)

        return cnt

#         arr = list(c)
#         for i in w:
#             if i in arr:
#                 arr.remove(i)
#                 if len(arr) == 0:
#                     return 1
#                 continue

#             else:
#                 return 0
#         return 1

#     def numMatchingSubseq(self, s, words):

#         count = 0
#         for i in words:
#             count+=self.find(i,s)

#         return count

ans = Solution()
s = "abcde"
words = ["a", "bb", "acd", "ace"]
print(ans.numMatchingSubseq(s,words))