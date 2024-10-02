# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):

        if root == None:
            return False

        stack = []
        stack.append([root, root.val])

        while len(stack) != 0:

            data = stack.pop()
            Node = data[0]
            Sum = data[1]

            if Node.left == None and Node.right == None and Sum == targetSum:
                return True

            if Node.right:
                stack.append([Node.right, Sum + Node.right.val])

            if Node.left:
                stack.append([Node.left, Sum + Node.left.val])

        return False


