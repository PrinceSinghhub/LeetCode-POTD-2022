# https://leetcode.com/problems/maximize-distance-to-closest-person/
class Solution:
    def maxDistToClosest(self, seats):
        First = 0
        temp = 0
        Second = None
        for s in seats:
            if s == 1:
                if Second == None:
                    Second = temp
                First = max(First, temp)
                temp = 0
            temp += 1

        return max(Second, First // 2, temp - 1)
ans = Solution()
seats = [1,0,0,0,1,0,1]
print(ans.maxDistToClosest(seats))