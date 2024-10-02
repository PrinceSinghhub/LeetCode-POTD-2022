class Solution:
    def reverseWords(self, s):
        r = s.split()
        r=r[::-1]
        output = " ".join(r)
        # return " ".join(s.split()[::-1])
        return output

