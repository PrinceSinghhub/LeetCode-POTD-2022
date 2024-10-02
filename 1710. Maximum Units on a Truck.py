class Solution:
    def maximumUnits(self, boxTypes, truckSize):

        boxTypes.sort(key=lambda x: x[1], reverse=1)
        print(boxTypes)
        s = 0
        for i, j in boxTypes:
            i = min(i, truckSize)
            s += i * j
            truckSize -= i
            if truckSize == 0:
                break
        return s

ans = Solution()
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 4
print(ans.maximumUnits(boxTypes,truckSize))