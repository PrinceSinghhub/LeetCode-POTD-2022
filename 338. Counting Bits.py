class Solution:
    def countBits(self, n):

        '''optimal solution
        ans = [0]*(n+1)

        for i in range(1,n+1):
            ans[i] = ans[i//2] + i%2

        return ans
        '''


        arr = []

        for i in range(n+1):

            Bin = str(bin(i))
            arr.append(Bin[2::])

        ans = []

        for i in arr:
            Char = i
            ans.append(Char.count('1'))
        return ans

ans = Solution()
n = 5
print(ans.countBits(n))

