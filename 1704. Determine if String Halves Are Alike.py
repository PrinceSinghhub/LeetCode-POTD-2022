class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']

        # initializing the first half of the word and the back half variables
        first, firstc = [*s][:len(s) // 2], 0
        back, backc = [*s][len(s) // 2:], 0

        # [*s] creates a list
        # [len(s)//2] finds the middle position of the list

        # counts the vowels in first and back half
        for x in first:
            if x.lower() in vowels:
                firstc += 1
        for y in back:
            if y.lower() in vowels:
                backc += 1
            # returns whether the counts are equal to each other
        return firstc == backc