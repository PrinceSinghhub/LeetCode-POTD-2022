# todo v.v.v.v.v.v imp question ask in MNC
class Solution:
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) < sum(cost):
            return -1

        else:
            difference = []
            for i in range(len(gas)):
                difference.append(gas[i] - cost[i])

            ArrayPrifx = []
            for i in difference:
                if len(ArrayPrifx) == 0:
                    ArrayPrifx.append(i)
                else:
                    add = ArrayPrifx[len(ArrayPrifx) - 1]
                    ans = add + i
                    ArrayPrifx.append(ans)

            ans = min(ArrayPrifx)
            if ArrayPrifx.index(ans) + 1 == len(ArrayPrifx):
                return 0
            else:
                return ArrayPrifx.index(ans) + 1

ans = Solution()
g = [3,1,1]
c = [1,2,2]
print(ans.canCompleteCircuit(g,c))
