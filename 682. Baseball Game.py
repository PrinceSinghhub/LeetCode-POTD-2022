class Solution:
    def calPoints(self, ops):

        ans = []

        for i in ops:
            if i.isdigit():
                ans.append(int(i))

            elif i == "C":
                ans.pop()

            elif i == "D":
                ans.append(ans[-1] * 2)

            elif i == "+":
                ans.append(ans[-1] + ans[-2])

            else:
                ans.append(int(i))
        print(ans)
        return sum(ans)

ans = Solution()
print(ans.calPoints(["5","-2","4","C","D","9","+","+","-2","4","C","D","9","+"]))
