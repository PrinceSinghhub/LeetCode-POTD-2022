class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Helper function to match the current character in the pattern with
        # the current position in the input string
        def match(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[i - 1] == '?':
                return True
            return s[j - 1] == p[i - 1]

        # Function to find the length of the longest suffix of the pattern
        # that matches the prefix of the input string
        def longest_suffix(i: int) -> int:
            l = 0
            while i >= 0 and p[i] == '*':
                l += 1
                i -= 1
            return l

        # Dynamic programming array to store the results of previous calls
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        # Initialize the first element to true, as the empty pattern matches the empty string
        dp[0][0] = True

        # Iterate over the pattern
        for i in range(1, len(p) + 1):
            # If the current character is a '*', set the corresponding element in the dp array to true if any of the
            # previous elements are true
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
                for j in range(1, len(s) + 1):
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            # Otherwise, set the corresponding element in the dp array to true if the previous element is true and
            # the current character in the pattern matches the current character in the input string
            else:
                for j in range(1, len(s) + 1):
                    dp[i][j] = dp[i - 1][j - 1] and match(i, j)

        # Return the last element in the dp array, which indicates whether the entire pattern matches the entire input string
        return dp[len(p)][len(s)]


