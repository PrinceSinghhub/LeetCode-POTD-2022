# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            nonlocal tail
            tail.right = node
            tail.left = None

            tail = tail.right
            tail.left = None

            inorder(node.right)
            tail.right = None

        ans = TreeNode(-1)
        tail = ans

        inorder(root)

        return ans.right


