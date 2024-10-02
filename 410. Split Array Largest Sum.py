class Solution:
    def splitArray(self, nums,m):

        start = 0
        end = 0

        for i in nums:
            start = max(start,i)
            end+=i

        while(start<end):
             mid = start+(end-start)//2
             sum = 0
             pices = 1

             for i in nums:
                 if(sum+i>mid):
                     sum = i
                     pices+=1
                 else:
                     sum+=i
             if pices>m:
                 start = mid+1
             else:
                 end = mid
        return end

ans = Solution()
nums = [7,2,5,10,8]
m = 2
print(ans.splitArray(nums,m))