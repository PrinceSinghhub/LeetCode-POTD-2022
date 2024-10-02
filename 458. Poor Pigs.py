from math import ceil, log


class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        ans = int(ceil(log(buckets) / log(minutesToTest / minutesToDie + 1)))
        return ans