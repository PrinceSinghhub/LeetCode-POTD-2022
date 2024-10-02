# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root):
        self.Sum = 0
        return self.inorderTraversal(root)

    def inorderTraversal(self, root):
        if root == None:
            return
        else:
            self.inorderTraversal(root.right)
            self.Sum += root.val
            root.val = self.Sum
            self.inorderTraversal(root.left)
            return root
