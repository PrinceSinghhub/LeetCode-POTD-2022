# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def InorderTraversal(node):

            if node == None:
                return []

            left = InorderTraversal(node.left)
            right = InorderTraversal(node.right)

            return left + [node] + right

        arr = InorderTraversal(root)

        ans = [i.val for i in arr]
        ans.sort()

        for i in range(len(ans)):
            arr[i].val = ans[i]

        return arr
        """
        Do not return anything, modify root in-place instead.
        """
