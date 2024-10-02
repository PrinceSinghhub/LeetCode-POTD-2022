class Solution:
    def concatenatedBinary(self, n: int) -> int:
        Bin = ''
        for i in range(1, n + 1):
            temp = bin(i)[2::]
            Bin += temp

        ans = int(Bin, 2)
        mod = 10 ** 9 + 7

        return ans % mod
