"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root == None:
            return []

        ans = []

        queue = deque([root])

        while queue:

            temp = []

            for i in range(len(queue)):
                Node = queue.popleft()
                temp.append(Node.val)

                for n in Node.children:
                    queue.append(n)
            ans += [temp]

        return ans
