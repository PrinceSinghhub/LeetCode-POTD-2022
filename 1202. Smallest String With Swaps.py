class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False  # already connected
        if prt > qrt: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True


class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        s = list(s)

        uf = UnionFind(len(s))
        for u, v in pairs:
            uf.union(u, v)

        mp = {}
        for n in range(len(s)):
            mp.setdefault(uf.find(n), []).append(n)

        for v in mp.values():
            vals = [s[vv] for vv in v]
            for vv, xx in zip(v, sorted(vals)):
                s[vv] = xx
        return "".join(s)