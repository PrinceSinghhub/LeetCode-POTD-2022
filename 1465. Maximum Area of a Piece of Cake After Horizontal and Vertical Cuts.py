class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):

        mod = int(1e9 + 7)

        print(mod)

        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        mh = horizontalCuts[0]
        mv = verticalCuts[0]
        for i in range(len(horizontalCuts) - 1):
            mh = max(mh, horizontalCuts[i + 1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            mv = max(mv, verticalCuts[i + 1] - verticalCuts[i])
        return (mh * mv) % mod

ans = Solution()

h = 5; w = 4; horizontalCuts = [1,2,4]; verticalCuts = [1,3]
print(ans.maxArea(h,w,horizontalCuts,verticalCuts))