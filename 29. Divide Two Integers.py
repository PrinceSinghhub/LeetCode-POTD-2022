import math


class Solution:
    def divide(self, dividend, divisor):
        res = dividend / divisor
        if res > 0:
            res = math.floor(res)
        else:
            res = math.ceil(res)
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < -2 ** 31:
            return -2 ** 31

        return int(res)


ans = Solution()
print(ans.divide(120,6))