class Solution:
    def romanToInt(self, s):

        letters = list(s)
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_let = 0
        prev = None
        for lets in letters:
            if prev is not None and romans[prev] < romans[lets]:
                sum_let += (romans[lets] - (romans[prev] * 2))
            else:
                sum_let += romans[lets]
            prev = lets
        return sum_let
