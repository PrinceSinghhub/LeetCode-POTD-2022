class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []

        for i in s:
            if i == '(':
                stack.append('(')

            else:
                current = 0
                while stack[-1] != '(':
                    current += stack[-1]
                    stack.pop()

                stack.pop()

                if current == 0:
                    stack.append(1)

                else:
                    stack.append(2 * current)

        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()

            stack.append(a + b)

        return stack[-1]

#         if s.count('(') == s.count(')'):

#             return s.count('(')



ans = Solution()
s = "()()()(())(())"
print(ans.scoreOfParentheses(s))
