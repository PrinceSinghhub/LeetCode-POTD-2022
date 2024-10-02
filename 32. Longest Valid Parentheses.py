class Solution:
    def longestValidParentheses(self, s):
        stack = []
        curLength = 0
        Max = 0
        for e in s:
            if e == ")":
                if len(stack) > 0:
                    curLength += stack.pop() + 2
                    Max = max(Max, curLength)
                else:
                    curLength = 0
            elif e == "(":
                stack.append(curLength)
                curLength = 0
        return Max

ans = Solution()
s = ")()())"
print(ans.longestValidParentheses(s))