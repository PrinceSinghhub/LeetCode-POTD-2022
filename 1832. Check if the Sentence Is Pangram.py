class Solution:
    def checkIfPangram(self, sentence):
        aplha = set(sentence)
        if(len(aplha)==26):
            return True
        else:
            return False