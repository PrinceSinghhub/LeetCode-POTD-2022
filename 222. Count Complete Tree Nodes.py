# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findLeftHeight(self, root):

        height = 0

        while root:
            height += 1
            root = root.left

        return height

    def findRightHeight(self, root):

        height = 0

        while root:
            height += 1
            root = root.right

        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        leftheight = self.findLeftHeight(root)
        rightheight = self.findRightHeight(root)

        if leftheight == rightheight:
            return (2 ** leftheight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
