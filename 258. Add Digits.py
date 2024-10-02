class Solution:
    def addDigits(self, num):

        # bruteforce Approch
        # def res(param):
        #     ans = 0
        #     while param > 0:
        #         ans += param % 10
        #         param = param // 10
        #     return ans
        #
        # while True:
        #     ans = res(num)
        #     if len(str(ans)) == 1:
        #         return ans
        #     num = ans

        if num == 0:
            return 0
        if num%9 == 9:
            return 9

        return num%9
ans = Solution()
n=123
print(ans.addDigits(n))


