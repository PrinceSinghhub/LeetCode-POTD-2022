class Solution:
    def findAnagrams(self, s, p):

        ans = []
        L = len(p)

        for i in range(len(s) - len(p)+1):
            check = s[i:i+L]
            a = self.checkAns(check,p)
            if a == True:
                ans.append(i)

        return ans

    def checkAns(self, check,p):

        arr = []
        for i in p:
            arr.append(i)
        ans = True
        for i in check:
            if i in arr:
                arr.remove(i)
                pass

            else:
                ans = False
        if ans == True:
            return True
        return False

ans = Solution()
s = "cbaebabacd"
p = "abc"
print(ans.findAnagrams(s,p))

