class Solution:
    def maxArea(self, height):

        low = 0
        highe = len(height) - 1

        Max = -1

        while low <= highe:

            temp = min(height[low], height[highe]) * (highe - low)
            Max = max(temp, Max)

            if height[low] < height[highe]:
                low += 1
            else:
                highe -= 1

        return Max

ans = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(ans.maxArea(height))



