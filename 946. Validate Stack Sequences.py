class Solution:
    def validateStackSequences(self, pushed, popped):

        stack = []

        index = 0

        n = len(pushed)

        for item in pushed:

            stack.append(item)

            while len(stack) > 0 and index < n and stack[-1] == popped[index]:
                stack.pop()

                index += 1

        return index == n

ans = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

print(ans.validateStackSequences(pushed,popped))