class Solution(object):
    def removeDuplicates(self, s, k):

        stack = [['0',0]]

        for item in s:
            if stack[-1][0] == item:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([item,1])

        stack.remove(stack[0])
        print(stack)

        ans = ''.join(key * val for key,val in stack)
        return ans



ans = Solution()
s = "abcd"
k = 2
print(ans.removeDuplicates(s,k))











