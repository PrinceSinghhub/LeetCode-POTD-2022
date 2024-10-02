class Solution:
    def detectCapitalUse(self, word):

        captial = 0
        small = 0
        mix = 0
        for i in word:
            if i.isupper():
                pass
            else:
               captial = 1
        if captial == 0:
            return  True

        else:
            for i in word:
                if i.islower():
                    pass
                else:
                    small = 1

        if small == 0:
            return True
        else:
            firstLetter = word[0]
            if firstLetter.isupper():
                mix+=1
            for i in range(1,len(word)):
                if word[i].islower():
                    mix+=1
        if mix == len(word):
            return True
        else:
            return False

ans = Solution()
word = "g"
print(ans.detectCapitalUse(word))
