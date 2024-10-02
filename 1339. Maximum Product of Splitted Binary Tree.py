from collections import defaultdict


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        stack, vals = [], []
        node, prev = root, None
        mp = defaultdict(int)
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if node.right and node.right != prev: node = node.right
                else:
                    mp[node] = node.val + mp[node.left] + mp[node.right]
                    vals.append(mp[node])
                    stack.pop()
                    prev = node
                    node = None
        return max(x*(vals[-1] - x) for x in vals) % 1_000_000_007