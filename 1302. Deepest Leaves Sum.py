class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        leaves_sum = list()
        queue = [(root, 0)]
        while queue:
            node, lvl = queue.pop()
            if not node:
                continue
            if lvl >= len(leaves_sum):
                leaves_sum.append(0)
            leaves_sum[lvl] += node.val
            queue += [(node.left, lvl+1), (node.right, lvl+1)]
        return leaves_sum[-1]

