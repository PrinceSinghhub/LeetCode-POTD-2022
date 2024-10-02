from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums):

        # optmize Approch

        arr = SortedList(nums)
        print(arr)
        ans = arr[-1] - arr[0]

        while arr[0] % 2 == 1:
            temp = arr[0]
            arr.remove(temp)
            arr.add(temp * 2)
            ans = min(ans, arr[-1] - arr[0])

        while arr[-1] % 2 == 0:
            temp = arr[-1]
            arr.remove(temp)
            arr.add(temp // 2)
            ans = min(ans, arr[-1] - arr[0])

        while arr[0] % 2 == 1:
            temp = arr[0]
            arr.remove(temp)
            arr.add(temp * 2)

            ans = min(ans, arr[-1] - arr[0])

        print(ans)

        return ans

        # bruteforce Approch
        for i in range(len(nums)):

            if nums[i]%2!=0:
                nums[i] = nums[i]*2

        print(nums)

        Minans = 99999999999999

        while True:
            MaxElement = max(nums)
            MinElement = min(nums)
            if MaxElement-MinElement<Minans:
                Minans = MaxElement-MinElement

            if MaxElement%2==0:
                reduce = MaxElement//2
                Index = nums.index(MaxElement)
                nums[Index] = reduce

            elif MaxElement%2!=0:
                if MaxElement*2-MinElement > Minans:
                    break

        print(nums)
        return Minans



ans = Solution()

nums = [4,1,5,20,3]
print(ans.minimumDeviation(nums))

