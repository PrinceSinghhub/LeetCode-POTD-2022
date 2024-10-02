class Solution(object):
    def removeKdigits(self, num, k):

        stack = []

        for n in num:
            while len(stack)!=0 and k > 0 and stack[-1] > n:
                k -= 1
                stack.pop()
            stack.append(n)

        while len(stack)!=0 and k > 0:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        print(stack)

        return str(int("".join(stack)))

ans = Solution()
num = "1432219"
k = 3
print(ans.removeKdigits(num,k))