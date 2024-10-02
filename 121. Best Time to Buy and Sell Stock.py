class Solution:
    def maxProfit(self, prices):

        # ans = []
        # for i in range(len(prices)):
        #     P = 0
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j]-prices[i]
        #         if profit>P:
        #             P = profit
        #     ans.append(P)
        # return max(ans)

       # optimize code
       Maxarr = [0]*len(prices)
       Maxarr[len(Maxarr)-1] = prices[len(prices)-1]

       for i in range(len(prices)-2,-1,-1):
           LastValue = Maxarr[i+1]
           Value = prices[i]
           Maxarr[i] = max(LastValue,Value)

       ans = 0
       for j in range(len(prices)):

           if Maxarr[j]-prices[j]>ans:
               ans = Maxarr[j]-prices[j]
       return ans




ans = Solution()
prices = [7,1,5,3,6,4]
print(ans.maxProfit(prices))



