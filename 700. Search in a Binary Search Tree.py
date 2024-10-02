# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):

        if root == None:
            return

        if root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)

        if root.val > val:
            return self.searchBST(root.left, val)
