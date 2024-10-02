class Solution:
    def removeCoveredIntervals(self, intervals):

        N = len(intervals)
        curved_Area = [False]*N

        for ri,(rx,ry) in enumerate(intervals):
            for ci, (cx, cy) in enumerate(intervals):
                if ri == ci:
                    continue

                if cx <= rx <=ry <= cy:
                    curved_Area[ri] = True
                    break

        print(curved_Area)
        return (curved_Area.count(False))


ans = Solution()

intervals =  [[1,4],[3,6],[2,8],[4,10],[6,11],[7,15],[9,14]]
print(ans.removeCoveredIntervals(intervals))

