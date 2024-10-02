# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []

        node = deque()
        node.append(root)

        while len(node) != 0:

            Sum = []
            for i in range(len(node)):
                Node = node.popleft()
                Sum.append(Node.val)

                if Node.left:
                    node.append(Node.left)

                if Node.right:
                    node.append(Node.right)

            ans.append(sum(Sum) / len(Sum))
        return ans

