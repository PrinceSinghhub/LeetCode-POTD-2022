from collections import defaultdict


class Solution:
    def criticalConnections(self, n, connections):
        cons = defaultdict(set)
        for a, b in connections:
            cons[a].add(b)
            cons[b].add(a)

        low = {}
        results = []

        def visit(node, from_node=None):
            if node in low: return low[node]
            cur_id = low[node] = len(low)

            for neigh in cons[node]:
                if neigh == from_node: continue
                low[node] = min(low[node], visit(neigh, node))

            if cur_id == low[node] and from_node is not None:
                results.append([from_node, node])
            return low[node]

        visit(0)
        return results
