class Solution:
    def guessNumber(self, n):

        first = 1
        last = n
        myGuess = last // 2
        ans = guess(myGuess)

        while ans != 0:
            if ans == -1:
                last = myGuess - 1
            else:
                first = myGuess + 1

            myGuess = (first + last) // 2
            ans = guess(myGuess)

        return myGuess
