class Solution:
    def findAndReplacePattern(self, words, pattern):

        result = []
        for word in words:
            if len(set(pattern)) == len(set(word)):
                tempDict = {}
                Flag = False
                for i in range(len(pattern)):
                    if pattern[i] not in tempDict:
                        Flag = True
                        tempDict[pattern[i]] = word[i]
                    elif pattern[i] in tempDict and tempDict[pattern[i]] != word[i]:
                        Flag = False
                        break
                if Flag == True:
                    result.append(word)
        return result


