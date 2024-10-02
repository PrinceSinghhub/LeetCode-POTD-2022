class Solution:
    def sequentialDigits(self, low,high):
        num = []
        for x in range(1, 9):
            while x <= high:
                r = x % 10

                if r == 0:
                    break

                if x >= low:
                    num.append(x)

                x = (x * 10) + r + 1

        return sorted(num)
ans = Solution()
a = 100
b = 300
print(ans.sequentialDigits(a,b))
