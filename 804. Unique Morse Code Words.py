class Solution:
    def uniqueMorseRepresentations(self, words):
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        output = set()
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in words:
            abc = ""
            for j in i:
                index = alpha.index(j)
                abc+=arr[index]
            output.add(abc)
        return len(output)