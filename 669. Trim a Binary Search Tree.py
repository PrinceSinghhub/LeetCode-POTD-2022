# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """

        def ans(node):

            if node is None:
                return None

            elif node.val < low:
                return ans(node.right)

            elif node.val > high:
                return ans(node.left)

            else:
                node.left = ans(node.left)
                node.right = ans(node.right)

                return node

        return ans(root)

