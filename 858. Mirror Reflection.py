from math import lcm


class Solution:
    def mirrorReflection(self, p, q):
        l = lcm(p, q)

        if (l // q) % 2 == 0:
            return 2
        return (l // p) % 2
