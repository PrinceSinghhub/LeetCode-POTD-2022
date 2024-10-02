class Solution:
    def checkInclusion(self, s1, s2):
        c = {}

        for ch in s1:
            c[ch] = c.get(ch, 0) + 1

        hm = {}
        sublen = 0

        for i, ch in enumerate(s2):
            hm[ch] = hm.get(ch, 0) + 1

            while hm[ch] > c.get(ch, 0):
                hm[s2[i - sublen]] -= 1
                sublen -= 1

            sublen += 1
            if sublen == len(s1):
                return True

        return False

ans = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(ans.checkInclusion(s1,s2))