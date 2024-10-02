# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):

        stack = [cloned]

        while stack != None:

            curr = stack.pop()

            if curr.val == target.val:
                return curr

            if curr.right != None:
                stack.append(curr.right)

            if curr.left != None:
                stack.append(curr.left)
