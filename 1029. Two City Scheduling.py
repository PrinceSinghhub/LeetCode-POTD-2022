class Solution:
    def twoCitySchedCost(self, costs):
        costs.sort(key = lambda x: x[0]-x[1])
        print(costs)
        total = 0
        for i in range(0, len(costs)):
            if i < len(costs)/2 :
                total += costs[i][0]
            else:
                total += costs[i][1]
        return total

ans = Solution()
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(ans.twoCitySchedCost(costs))
