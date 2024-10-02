class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size < 2: return 0
        hold, unhold, cooldown = float('-inf'),0,0
        for price in prices:
            hold=max(hold,cooldown-price)
            cooldown = max(cooldown, unhold)
            unhold=max(unhold,hold+price)
        return unhold