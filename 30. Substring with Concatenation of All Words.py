from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: 'List[str]') -> 'List[int]':
        if not words:
            return []

        word_len, res = len(words[0]), []

        # start offset from 0 to word_len, and step is word_len
        for i in range(word_len):
            # reset state every epoch
            # counter maintain current state
            counter = Counter(words)
            # two-pointer as boundary of sliding window to traverse, and count as condition checker, update it when trigger some key changes
            start, end, count = i, i, len(words)
            while end < len(s):
                cur_word = s[end:end + word_len]
                # check is not necessary here, just for performance
                if cur_word in counter:
                    counter[cur_word] -= 1
                    if counter[cur_word] >= 0:
                        count -= 1
                end += word_len

                if count == 0:
                    res.append(start)

                # ensure consecutive words
                if end - start == word_len * len(words):
                    cur_word = s[start:start + word_len]
                    if cur_word in counter:
                        counter[cur_word] += 1
                        if counter[cur_word] > 0:
                            count += 1
                    start += word_len

        # the order is not necessary here
        return res
