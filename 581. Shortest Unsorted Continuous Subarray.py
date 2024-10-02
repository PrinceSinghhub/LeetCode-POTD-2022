class Solution(object):
    def findUnsortedSubarray(self, nums):

        index = []
        temp = sorted(nums)
        for i in range(len(nums) - 1):

            if nums[i] != temp[i]:
                index.append(i)
                break

        for i in range(len(nums) - 1, -1, -1):

            if nums[i] != temp[i]:
                index.append(i)
                break

        print(index)

        if sum(index) > 0 and len(index) > 1:
            return sum(index)+1

        return 0




ans = Solution()
arr = [1,2,5,3,4,9,6,11,13,4,90,0,88,99,100,110]
print(ans.findUnsortedSubarray(arr))