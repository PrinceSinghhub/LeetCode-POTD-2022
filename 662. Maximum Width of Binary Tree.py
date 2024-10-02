# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):

        if not root:
            return 0

        q = [(root, 1)]

        res = 1
        lastNode = root
        while len(q) > 0:
            node, idx = q.pop(0)

            if node.left:
                q.append((node.left, idx * 2))
            if node.right:
                q.append((node.right, idx * 2 + 1))

            if node == lastNode:
                if len(q) > 0:
                    res = max(res, q[-1][1] - q[0][1] + 1)
                    lastNode = q[-1][0]

        return res
