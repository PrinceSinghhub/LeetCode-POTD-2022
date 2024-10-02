# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s):

        s = s.strip()
        Minus = 0
        number = ""

        for index,char in enumerate(s):
            if index == 0:
                if char == "-":
                    Minus = 1
                    continue
                if char == "+":
                    continue
            if char.isdigit():
                number+=char
            else:
                break

        number = 0 if not number else int(number)


        if Minus == 1:
            return max(-2**31,-number)
        return min(2**31-1,number)

ans = Solution()
s = "91283472332"
# s = "-910 6"
print(ans.myAtoi(s))

