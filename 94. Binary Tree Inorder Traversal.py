# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        stack = []
        currentNode = root

        ans = []

        while True:

            if currentNode != None:
                stack.append(currentNode)
                currentNode = currentNode.left


            else:
                if len(stack) == 0:
                    break
                rootNode = stack.pop()
                ans.append(rootNode.val)
                currentNode = rootNode.right

        return ans



